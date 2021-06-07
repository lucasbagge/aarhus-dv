INTRODUKTION TIL PROGRAMMERING MED VIDENSKABELIGE ANVENDELSER
=============================================================

  * Eksamen 26. juni 2020, 9:00-15:00.

  * Hjælpemidler: alle, inkl. internet.

  * Det er ikke lovligt at kommunikere med andre om eksamensopgaverne
    under eksamen.

  * Sørg for at angive en kommentar i koden med en kildehenvisning,
    hvis man anvender kode man har fundet på internettet.

  * Opgaveformulering hentes og afleveres på eksamen.au.dk.

      Filer der udleveres til eksamen:

      A.py, B.py...: Opgaver. Formuleringerne fremgår af doc-teksten i
                     starten af filerne. En eksamensbesvarelse består af
                     upload af disse filer med indsat kode.

      tests        : Folder med eksempler på test input og korrekte svar
                     for alle opgaver.

      run_tests.py : Et program til at køre alle de udleverede tests.

  * Vægtningen af opgaverne:

     Problem  Point  Navn
        A       4    REVERSE STRING
        B       4    COUNT
        C       5    FUNCTION TABLE
        D       5    WALK
        E       7    TREE MIRROR
        F       9    MISSING RECTANGLE CORNER
        G      10    POSITION TRACKER
        H       8    UNIQUE VALUES
        I       8    VECTOR SORT
        J      10    SOCCER TOURNAMENT
        K      10    REACHABLE POSITIONS
        L      10    RECURSIVE FUNCTION
        M      10    INTERPOLATION

    Totalt 100 point

  * Aflevering:

      Aflevering skal være en zip fil med opgaverne

         A.py, B.py, ... og filen run_tests.log.

      Man må meget gerne aflevere hele ens folder incl. test cases og
      ubesvarede opgaver.

      Inden man afleverer bør man køre run_tests.py en sidste gang på
      alle ens besvarelser. Resultatet af testene gemmes løbende i
      run_tests.log. Som kontrol, vil indholdet af run_tests.log (hvis
      denne afleveres) blive sammenholdet med resultatet af den
      efterfølgende evaluering.
 
  * Opgaverne skal laves i Python 3.8. Der må kun bruges de standard
    moduler der følger med Python (f.eks. random, math, collections,
    etc.), såfremt der ikke er nævnt specifikke andre moduler i
    opgaveformuleringen.

  * Eksamensbesvarelsen kan IKKE afleveres i en Jupyter Notebook.

  * Aflevering skal være som en .zip fil, gerne hele eksamensfolderen
    med tests, ikke besvarede opgaver etc. Information om hvordan
    man laver en zip fil under macOS og Windows 10 findes her:

     https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac
     https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files

  * Hvis digital eksamen skulle finde på at spørge om antal anslag i
    ens aflevering, hvilket ikke giver mening for denne eksamen, så
    er svaret 42.

  * Pointfordeling af opgaverne fremgår af __README__ filen.

  * I opgavebeskrivelser er der angivet nogle input betingelser,
    f.eks. at 1 <= n <= 10. Det er en garanti som alle test input vil
    opfylde. Det er ikke noget man behøver checke for (med
    assertions eller lignende).

  * De skjulte input vil også overholde input betingelserne.

  * Når man læser en linje fra input med input(), har nogle Mac
    brugere oplevet problemer med at linjerne slutter med '\r' i
    deres programmer.  Hvis man anvender input().strip() vil disse
    '\r' blive fjernet. Scriptet run_tests.py er opdateret til at
    forsøge at undgå disse problemer med '\r' i input på en Mac.

  * run_tests.pl kan køres på forskellige måder, hvilket beskrives i
    starten af filen). En mulig løsning er at udkommentere linjen

       DEFAULT_FILES = ['A', 'B', 'C']

    og angive navnene på de filer der skal testes.

  * I anbefales at aflevere den fulde run_tests.log fil, selvom den
    kan blive lidt lang. Hvis I aflevere den, vil jeg bruge den til
    at verificere at min test af jeres besvarelse giver mening.
    Hvis der er i log-filen er en entry om at et testinput på et
    tidspunkt er blevet accepteret, men min efterfølgende test ikke
    godkender dette testinput, så vil jeg undre mig og følge op -
    specielt hvis det er den sidste kørsel af dette testinput der
    slår ud.

  * Jeg har valgt at skrive at default er at man kun må bruge standard
    Python bibliotekker. Ellers ville jeg skulle skrive det i de
    fleste opgaver, og alle studerende skulle læse det igen-og-igen.
    De fleste opgaver vil kunne løses med få linjers ren Python kode,
    uden brug af nogen biblioteker.

  * Er kode-strukturen/læsbarheden ligegyldig til eksamen? Fokuseres
    der udelukkende på dets funktionalitet, altså antal tests det
    accepterer?
    
    Svar: Kun tests. Men velstruktureret kode har nok større
          sandsynlighed for at virke.

    Er det forventet vi skriver forklarende kommentarer til vores kode
    til eksamen?

    Svar: Nej, dog skal man huske at skrive en kommentar med
          kildehenvisning hvis man kopierer kode fra internettet.

  * SKAL eksamen afleveres som .zip-fil? Ja, en .zip fil - please!
    (Hvis andet afleveres skal jeg nok forsøge at få det til at virke.
    Til nød må jeg skrive til den studerende og få hjælp med at pakke
    ud -  håber ikke det bliver relevant!).

  * test_run.py stopper jeres program efter 5 sekunder, men det burde
    være rigeligt til at løse de fleste test instanser. I enkelte
    opgaver kan nogle af test instanserne dog kræve at man har en
    tilstrækkelig hurtig løsning for at få de sidste test instanser
    godkendt. Jeg vil tillade lidt mere tid når jeg evaluerer jeres
    programmer. 
    
  * Officielt, så er det Python version 3.8 man bør bruge. Men jeg
    forsøger at undgå at lave afhængigheder i opgaveformuleringen, der
    specifikt vil kræve 3.8 (f.eks. := og f'{x=}'), så jeg forventer
    ikke det bliver et problem hvis man kun har Python 3.7 på sin
    maskine.

  * Man får ikke point for at håndtere input ved at hard code input
    instanser og deres svar. For hvert input må man forvente at der
    vil være et hemmeligt input af samme "type", så hvis man klarer et
    input så skal man også klare det tilsvarende skjulte input -
    ellers må jeg ind og kigge på koden.

  * Der vil være 10-15 opgaver til eksamen.

  * Jeg forventer at karaktererne kan være tilgængelig den 30. juni.

Held og lykke med eksamen
Gerth
