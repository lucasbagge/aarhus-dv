INTRODUKTION TIL PROGRAMMERING MED VIDENSKABELIGE ANVENDELSER
=============================================================

  * Reeksamen august 2020.

  * Hj�lpemidler: alle, inkl. internet.

  * Det er ikke lovligt at kommunikere med andre om eksamensopgaverne
    under eksamen.

  * S�rg for at angive en kommentar i koden med en kildehenvisning,
    hvis man anvender kode man har fundet p� internettet.

  * Opgaveformulering hentes og afleveres p� eksamen.au.dk.

      Filer der udleveres til eksamen:

      A.py, B.py...: Opgaver. Formuleringerne fremg�r af doc-teksten i
                     starten af filerne. En eksamensbesvarelse best�r af
                     upload af disse filer med indsat kode.

      tests        : Folder med eksempler p� test input og korrekte svar
                     for alle opgaver.

      run_tests.py : Et program til at k�re alle de udleverede tests.

  * V�gtningen af opgaverne:

     Problem  Point  Navn
        A       6    SPLIT STRING
        B       6    INTERVAL SUM
        C       6    STRING LENGTHS
        D       7    DIVISIBLE
        E       7    SQUARES
        F       8    VOWEL SORTING
        G      10    BROKEN FUNCTION
        H      10    PLOT FUNCTION
        I      10    CALCULATOR CLASS
        J      10    ITERABLE Z-COUNT
        K      10    SMOOTH
        L      10    COIN COLLECTOR

    Totalt 100 point

  * Aflevering skal v�re en zip fil med opgaverne

       A.py, B.py, ... og filen run_tests.log.

    Man m� meget gerne hele eksamensfolderen med tests, ikke
    besvarede opgaver etc.
    
    Information om hvordan man laver en zip fil under macOS og
    Windows 10 findes her:

       https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac
       https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files

    Inden man afleverer b�r man k�re run_tests.py en sidste gang p�
    alle ens besvarelser. Resultatet af testene gemmes l�bende i
    run_tests.log. Som kontrol, vil indholdet af run_tests.log blive
    sammenholdet med resultatet af den efterf�lgende evaluering.
 
  * Opgaverne skal laves i Python 3.8. Der m� kun bruges de standard
    moduler der f�lger med Python (f.eks. random, math, collections,
    etc.), s�fremt der ikke er n�vnt specifikke andre moduler i
    opgaveformuleringen.

  * Eksamensbesvarelsen kan IKKE afleveres i en Jupyter Notebook.

  * I opgavebeskrivelser er der angivet nogle input betingelser,
    f.eks. at 1 <= n <= 10. Det er en garanti som alle test input vil
    opfylde. Det er ikke noget man beh�ver checke for (med assertions
    eller lignende).  De skjulte input vil ogs� overholde disse input
    betingelser.

  * run_tests.pl kan k�res p� forskellige m�der, hvilket beskrives i
    starten af filen. En mulig l�sning er at udkommentere linjen

       DEFAULT_FILES = ['A', 'B', 'C']

    og angive navnene p� de filer der skal testes.

  * Er kode-strukturen/l�sbarheden ligegyldig til eksamen? Fokuseres
    der udelukkende p� dets funktionalitet, alts� antal tests det
    accepterer?
    
    Svar: Ja. Men velstruktureret kode har nok st�rre sandsynlighed
          for at virke.

    Er det forventet vi skriver forklarende kommentarer til vores kode
    til eksamen?

    Svar: Nej. Dog skal man huske at skrive en kommentar med
          kildehenvisning hvis man kopierer kode fra internettet.

  * test_run.py stopper jeres program efter 5 sekunder, men det burde
    v�re rigeligt til at l�se de fleste test instanser. I enkelte
    opgaver kan nogle af test instanserne dog kr�ve at man har en
    tilstr�kkelig hurtig l�sning for at f� de sidste test instanser
    godkendt. Til den efterf�lgende evaluering af programmerne vil der
    blive tilladt lidt mere tid.
    
  * Man f�r ikke point for at h�ndtere input ved at hard code input
    instanser og deres svar. For hvert input m� man forvente at der
    vil v�re et hemmeligt input af samme "type", s� hvis man klarer et
    input s� b�r man ogs� klare det tilsvarende skjulte input.
