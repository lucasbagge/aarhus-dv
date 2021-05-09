## app.R ##
library(shiny)
library(shinydashboard)
library(quantmod)
library(highcharter)
library(dplyr)
library(magrittr)
library(tidyquant)
library(ggplot2)
library(plotly)

ui <- dashboardPage(
  dashboardHeader(),
  dashboardSidebar(
    selectInput("stock_id", 
                "DAX Stock:",
                c("BAVA.CO",
                  "GMAB.CO",
                  "ORSTED.CO",
                  "CHR.CO",
                  "VWS.CO",
                  "CARL-B.CO",
                  "NOVO-B.CO",
                  "FLS.CO",
                  "JYSK.CO",
                  "DANSKE.CO",
                  "TRYG.CO"))
  ),
  dashboardBody(
    fluidRow(
      box(highchartOutput("plot1"), width = "100%", height = "100%"),
      box(plotOutput("plot2")),
      box(plotOutput("plot3")),
      box(plotOutput("plot4")),
      box(highchartOutput("plot5"))
    )
  )
)

server <- function(input, output) { 
  #SPY_tibble <- tq_get("ORSTED.CO", get="stock.prices")
  SPY_tibble_1 <- reactive({
    SPY_tibble <- tq_get(input$stock_id, get="stock.prices")
    SPY_tibble %>% 
      tq_mutate(select = c(close), mutate_fun = SMA, n = 12) %>% 
      rename(SMA_12 = SMA) %>% 
      tq_mutate(select = c(close), mutate_fun = SMA, n = 5) %>% 
      rename(SMA_5 = SMA) %>% 
      tq_mutate(select = c(close), mutate_fun = SMA, n = 50) %>% 
      mutate(sma5tr_tibble = Lag(case_when(
        Lag(close) < Lag(SMA) & close > SMA ~ 1,
        Lag(close) > Lag(SMA) & close < SMA ~ -1,
        TRUE ~ 0))) %>% 
      tq_mutate(select     = close, 
                mutate_fun = MACD, 
                nFast      = 12, 
                nSlow      = 26, 
                nSig       = 9, 
                maType     = SMA) %>%
      mutate(diff = macd - signal) %>% 
      tq_mutate(select = c(close), mutate_fun = RSI, n = 10, maType = SMA)
  })
  
    
  
  output$plot1 <- renderHighchart({
    highchart(type = "stock") %>% 
      # hc_yAxis_multiples(
      #   create_yaxis(2, height = c(2, 1), turnopposite = TRUE)
      # ) %>% 
      hc_add_series(SPY_tibble_1() %>% timetk::tk_xts(date_var = "date"), 
                    #yAxis = 0,
                    name = "SPY")  %>% 
      hc_add_series(SPY_tibble_1() %>% 
                      select(date, SMA) %>% 
                      timetk::tk_xts(date_var = "date"),
                    #yAxis = 0, 
                    name = "SMA - 50") %>% 
      hc_add_series(SPY_tibble_1() %>% 
                      select(date, SMA_12) %>% 
                      timetk::tk_xts(date_var = "date"),
                    #yAxis = 0, 
                    name = "SMA - 200") %>% 
      hc_add_series(SPY_tibble_1() %>% 
                      select(date, SMA_5) %>% 
                      timetk::tk_xts(date_var = "date"),
                    #yAxis = 0, 
                    name = "SMA - 5")
  })
  
  output$plot2 <- renderPlot({
    SPY_tibble_1() %>%
      filter(date > "2020-06-01") %>% 
      ggplot(aes(x = date)) + 
      geom_hline(yintercept = 0, color = palette_light()[[1]]) +
      geom_line(aes(y = macd)) +
      geom_line(aes(y = signal), color = "blue", linetype = 2) +
      geom_bar(aes(y = diff), stat = "identity", color = palette_light()[[1]]) +
      labs(title = "FANG: Moving Average Convergence Divergence",
           y = "MACD", x = "", color = "") +
      theme_tq() +
      scale_color_tq()
  })
  
  output$plot3 <- renderPlot({
    SPY_tibble_1() %>% 
      filter(date > "2020-06-01") %>% 
      ggplot(aes(x=date,y=rsi)) +
      geom_line(color = "blue", size=0.8) +
      geom_hline(yintercept = 30, color="red", size=2) +
      geom_hline(yintercept = 70, color="green",size=2) +
      labs(title="Relative Strength Index", y = "RSI", x="") +
      theme_tq()
  })
  
  output$plot4 <- renderPlot({
    SPY_tibble_1() %>%
      filter(date > "2020-06-01") %>% 
      ggplot(aes(x = date, y = close, open = open,
                 high = high, low = low, close = close)) +
      geom_candlestick() +
      geom_bbands(ma_fun = SMA, sd = 2, n = 20, 
                  linetype = 4, size = 1, alpha = 0.2, 
                  fill        = palette_light()[[1]], 
                  color_bands = palette_light()[[1]], 
                  color_ma    = palette_light()[[2]]) +
      labs(title = "AAPL Candlestick Chart", 
           subtitle = "BBands with SMA Applied, Experimenting with Formatting", 
           y = "Closing Price", x = "")  +
      theme_tq()
  })
  
  output$plot5 <- renderHighchart({
    SPY_tibble_1() %>% 
      filter(date > "2020-06-01") %>% 
      tq_mutate(select     = c(high, low, close), 
                mutate_fun = SMI, 
                n = 10,
                nFast = 5, 
                nSlow = 3,
                nSig = 30) %>% 
      mutate(higher_value = 40,
             buffer_lowr = -15,
             buffer_higher = 15) %>% 
      tidyr::pivot_longer(
        cols = c("SMI", "signal", "higher_value", "buffer_lowr", "buffer_higher"),
        names_to = "Indicator", 
        values_to = "Indicator_value"
      )  %>% 
      hchart("line", hcaes(date, Indicator_value, group = Indicator)) %>% 
      highcharter::hc_yAxis(plotLines = list(list(value = c(-40), color = "red", width = 2,
                                                  dashStyle = "shortdash")))
  })
}

shinyApp(ui, server)
