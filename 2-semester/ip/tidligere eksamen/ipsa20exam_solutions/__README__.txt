INTRODUKTION TIL PROGRAMMERING MED VIDENSKABELIGE ANVENDELSER
=============================================================

  * Eksamen 26. juni 2020, 9:00-15:00.

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

      Aflevering skal v�re en zip fil med opgaverne

         A.py, B.py, ... og filen run_tests.log.

      Man m� meget gerne aflevere hele ens folder incl. test cases og
      ubesvarede opgaver.

      Inden man afleverer b�r man k�re run_tests.py en sidste gang p�
      alle ens besvarelser. Resultatet af testene gemmes l�bende i
      run_tests.log. Som kontrol, vil indholdet af run_tests.log (hvis
      denne afleveres) blive sammenholdet med resultatet af den
      efterf�lgende evaluering.
 
  * Opgaverne skal laves i Python 3.8. Der m� kun bruges de standard
    moduler der f�lger med Python (f.eks. random, math, collections,
    etc.), s�fremt der ikke er n�vnt specifikke andre moduler i
    opgaveformuleringen.

  * Eksamensbesvarelsen kan IKKE afleveres i en Jupyter Notebook.

  * Aflevering skal v�re som en .zip fil, gerne hele eksamensfolderen
    med tests, ikke besvarede opgaver etc. Information om hvordan
    man laver en zip fil under macOS og Windows 10 findes her:

     https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac
     https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files

  * Hvis digital eksamen skulle finde p� at sp�rge om antal anslag i
    ens aflevering, hvilket ikke giver mening for denne eksamen, s�
    er svaret 42.

  * Pointfordeling af opgaverne fremg�r af __README__ filen.

  * I opgavebeskrivelser er der angivet nogle input betingelser,
    f.eks. at 1 <= n <= 10. Det er en garanti som alle test input vil
    opfylde. Det er ikke noget man beh�ver checke for (med
    assertions eller lignende).

  * De skjulte input vil ogs� overholde input betingelserne.

  * N�r man l�ser en linje fra input med input(), har nogle Mac
    brugere oplevet problemer med at linjerne slutter med '\r' i
    deres programmer.  Hvis man anvender input().strip() vil disse
    '\r' blive fjernet. Scriptet run_tests.py er opdateret til at
    fors�ge at undg� disse problemer med '\r' i input p� en Mac.

  * run_tests.pl kan k�res p� forskellige m�der, hvilket beskrives i
    starten af filen). En mulig l�sning er at udkommentere linjen

       DEFAULT_FILES = ['A', 'B', 'C']

    og angive navnene p� de filer der skal testes.

  * I anbefales at aflevere den fulde run_tests.log fil, selvom den
    kan blive lidt lang. Hvis I aflevere den, vil jeg bruge den til
    at verificere at min test af jeres besvarelse giver mening.
    Hvis der er i log-filen er en entry om at et testinput p� et
    tidspunkt er blevet accepteret, men min efterf�lgende test ikke
    godkender dette testinput, s� vil jeg undre mig og f�lge op -
    specielt hvis det er den sidste k�rsel af dette testinput der
    sl�r ud.

  * Jeg har valgt at skrive at default er at man kun m� bruge standard
    Python bibliotekker. Ellers ville jeg skulle skrive det i de
    fleste opgaver, og alle studerende skulle l�se det igen-og-igen.
    De fleste opgaver vil kunne l�ses med f� linjers ren Python kode,
    uden brug af nogen biblioteker.

  * Er kode-strukturen/l�sbarheden ligegyldig til eksamen? Fokuseres
    der udelukkende p� dets funktionalitet, alts� antal tests det
    accepterer?
    
    Svar: Kun tests. Men velstruktureret kode har nok st�rre
          sandsynlighed for at virke.

    Er det forventet vi skriver forklarende kommentarer til vores kode
    til eksamen?

    Svar: Nej, dog skal man huske at skrive en kommentar med
          kildehenvisning hvis man kopierer kode fra internettet.

  * SKAL eksamen afleveres som .zip-fil? Ja, en .zip fil - please!
    (Hvis andet afleveres skal jeg nok fors�ge at f� det til at virke.
    Til n�d m� jeg skrive til den studerende og f� hj�lp med at pakke
    ud -  h�ber ikke det bliver relevant!).

  * test_run.py stopper jeres program efter 5 sekunder, men det burde
    v�re rigeligt til at l�se de fleste test instanser. I enkelte
    opgaver kan nogle af test instanserne dog kr�ve at man har en
    tilstr�kkelig hurtig l�sning for at f� de sidste test instanser
    godkendt. Jeg vil tillade lidt mere tid n�r jeg evaluerer jeres
    programmer. 
    
  * Officielt, s� er det Python version 3.8 man b�r bruge. Men jeg
    fors�ger at undg� at lave afh�ngigheder i opgaveformuleringen, der
    specifikt vil kr�ve 3.8 (f.eks. := og f'{x=}'), s� jeg forventer
    ikke det bliver et problem hvis man kun har Python 3.7 p� sin
    maskine.

  * Man f�r ikke point for at h�ndtere input ved at hard code input
    instanser og deres svar. For hvert input m� man forvente at der
    vil v�re et hemmeligt input af samme "type", s� hvis man klarer et
    input s� skal man ogs� klare det tilsvarende skjulte input -
    ellers m� jeg ind og kigge p� koden.

  * Der vil v�re 10-15 opgaver til eksamen.

  * Jeg forventer at karaktererne kan v�re tilg�ngelig den 30. juni.

Held og lykke med eksamen
Gerth
