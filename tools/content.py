# -*- coding: utf-8 -*-
"""All copy for the SpotShield website, English and Slovenian.
Edit here, then run `python3 tools/build.py` to regenerate index.html and sl/index.html."""

APP_IDS = ['carp', 'fly', 'predator', 'sea', 'hunter', 'mushroom', 'birder', 'treasure']
STORE_NAMES = {
    'carp': 'SpotShield Carp', 'fly': 'SpotShield Fly Fishing', 'predator': 'SpotShield Predator',
    'sea': 'SpotShield Sea Fishing', 'hunter': 'SpotShield Hunter', 'mushroom': 'SpotShield Mushroom',
    'birder': 'SpotShield Birder', 'treasure': 'SpotShield Treasure',
}
SHORT_NAMES_EN = {
    'carp': 'Carp', 'fly': 'Fly Fishing', 'predator': 'Predator', 'sea': 'Sea Fishing',
    'hunter': 'Hunter', 'mushroom': 'Mushroom', 'birder': 'Birder', 'treasure': 'Treasure',
}
PLAY_URL = 'https://play.google.com/store/apps/details?id=si.spotshield.{id}'
PRIVACY_URL = 'https://deniskorinsek.github.io/spotshield-privacy/{id}/'
PRIVACY_INDEX = 'https://deniskorinsek.github.io/spotshield-privacy/'
CONTACT = 'korinsekdenis+play@gmail.com'

EN = {
    'lang': 'en', 'locale': 'en_GB', 'other_lang': 'sl', 'other_href': 'sl/', 'other_label': 'Slovenščina',
    'title': 'SpotShield — Share the moment. Not the place.',
    'description': 'Eight Android apps that find and cover the clues that give your spot away — GPS data, signs, number plates, screens — right on your phone. No internet permission, no account, no analytics.',
    'nav': {
        'aria': 'Main', 'brand_aria': 'SpotShield, back to top', 'apps': 'Apps', 'how': 'How it works', 'privacy': 'Privacy',
        'cta': 'Get the apps', 'lang_aria': 'Language', 'menu': 'Menu',
        'theme_dark': 'Switch to light mode', 'theme_light': 'Switch to dark mode',
    },
    'hero': {
        'eyebrow': 'Eight Android apps · Photo privacy for the outdoors',
        'h1a': 'Share the moment.', 'h1b': 'Not the place.',
        'lede': 'One photo can give your spot away — GPS in the file, a sign, a number plate, a screen in the background. SpotShield finds these clues and covers them before you share. One app for each hobby, all on your phone.',
        'picker': 'Choose your hobby', 'picker_aria': 'The eight SpotShield apps',
        'primary': 'Get the apps', 'secondary': 'See it work',
        'trust': 'No internet permission · No account · No analytics',
        'deck_aria': 'The eight apps, one at a time',
    },
    'apps': {
        'eyebrow': 'The apps · Android', 'h2': 'Eight apps. One promise.',
        'lede': 'Each app speaks the language of its hobby — peg numbers, beat signs, high seats and hides — and keeps the same promise: the place stays yours.',
        'play': 'Google Play', 'play_aria': 'Get {name} on Google Play', 'priv': 'Privacy', 'priv_aria': '{name} privacy policy',
        'items': {
            'carp':     dict(aud='Carp anglers',     kicker='Privacy for anglers',          l1='Share the PB.',       l2='Not the swim.',  alt='A carp angler at dusk holding a mirror carp by a lake'),
            'fly':      dict(aud='Fly anglers',      kicker='Privacy for fly anglers',      l1='Share the trout.',    l2='Not the pool.',  alt='A trout held over a clear alpine river, a fly angler wading behind'),
            'predator': dict(aud='Predator anglers', kicker='Privacy for predator anglers', l1='Share the pike.',     l2='Not the spot.',  alt='A pike held up over a lake at sunset'),
            'sea':      dict(aud='Sea anglers',      kicker='Privacy for sea anglers',      l1='Share the catch.',    l2='Not the mark.',  alt='A sea bream held up at a sunny marina'),
            'hunter':   dict(aud='Hunters',          kicker='Privacy for hunters',          l1='Share the hunt.',     l2='Not the stand.', alt='A red deer stag in a hunting ground at dawn, a high seat behind'),
            'mushroom': dict(aud='Mushroom pickers', kicker='Privacy for mushroom pickers', l1='Share the basket.',   l2='Not the patch.', alt='A basket of porcini mushrooms on a forest trail'),
            'birder':   dict(aud='Birders',          kicker='Privacy for birders',          l1='Share the sighting.', l2='Not the roost.', alt='A kingfisher on a branch in a reed-lined nature reserve'),
            'treasure': dict(aud='Detectorists',     kicker='Privacy for detectorists',     l1='Share the find.',     l2='Not the field.', alt='A coin held up over a ploughed field, a metal detector beside it'),
        },
    },
    'demo': {
        'eyebrow': 'See it work', 'h2': 'One photo. Five clues. Gone.',
        'lede': 'Drag the handle. On the left, the original with everything SpotShield Carp found. On the right, the protected copy it made — on the phone, in seconds.',
        'before': 'Before', 'after': 'After', 'gps': 'GPS in file', 'ok': 'Location data removed', 'hint': 'Drag to compare',
        'range_aria': 'Compare the original photo with the protected copy',
        'alt_before': 'Original photo of a carp angler at dusk. SpotShield marks a possible vehicle plate, a sign with text, a QR code, a peg marker and a GPS screen.',
        'alt_after': 'Protected copy: the plate and the GPS screen are covered, the sign and the peg marker are blurred, the QR code is pixelated and the location data is removed.',
        'found': [
            ('pin', 'Location stored in the file', 'Removed'),
            ('plate', 'Number plate on the car', 'Covered'),
            ('screen', 'GPS screen on the bait boat handset', 'Covered'),
            ('sign', 'Lake sign and peg marker', 'Blurred'),
            ('qr', 'QR code on the bucket', 'Pixelated'),
        ],
        'note': 'Cover, pixelate, blur or fill — you choose for each area, or protect every risky one in a single tap. The photo in your gallery stays as it was.',
    },
    'how': {
        'eyebrow': 'How it works', 'h2': 'Scan. Review. Protect. Share.',
        'lede': 'From the photo you’re proud of to a copy that’s safe to post — all on your phone.',
        'steps': [
            ('Scan', 'Choose a photo, share one from another app or take one with the SpotShield camera. Six checks run on the phone.', 'SpotShield Fly Fishing scanning a photo: three of six checks done'),
            ('Review', 'See everything that could reveal the place, from location data in the file to a sign far in the background.', 'SpotShield Carp risk report: 78 out of 100, high risk'),
            ('Protect', 'Cover, pixelate, blur or fill each area — or protect every risky one in a single tap. Fill rebuilds the area from its surroundings.', 'SpotShield Birder findings: choose cover, pixelate, blur or fill for each area'),
            ('Share', 'Get a new copy without location data, checked once more before you share. The photo in your gallery stays as it was.', 'SpotShield Treasure: your protected copy is ready, with every check passed'),
        ],
        'checks_title': 'What SpotShield looks for',
        'checks': [
            ('pin', 'Location data in the file'), ('sign', 'Signs and text'), ('plate', 'Number plates'),
            ('screen', 'Map and sonar screens'), ('qr', 'QR codes and barcodes'), ('city', 'Buildings and skylines'),
            ('video', 'Hidden video in motion photos'),
        ],
    },
    'privacy': {
        'eyebrow': 'Privacy', 'h2': 'Your photos never leave your device.',
        'lede': 'Every app checks and protects your photos on your phone, even offline. The apps don’t have internet permission, so nothing can be uploaded — not to us, not to anyone.',
        'pillars': [
            ('offline', 'No internet permission', 'Android keeps the apps offline, so nothing can be uploaded.'),
            ('noaccount', 'No account', 'No sign-up, no email, no profile.'),
            ('noanalytics', 'No analytics, no ads', 'The only permissions are the camera and, for “Check original”, the photo’s own location tag — both optional.'),
        ],
        'art_aria': 'Illustration: a phone with a photo sits inside a shield; ripples spread around it, while a cloud and a map pin are crossed out.',
    },
    'limits': {
        'eyebrow': 'Honest limits', 'h2': 'What SpotShield can’t see',
        'lede': 'Some clues are beyond any app. Check these yourself before you share.',
        'items': [
            ('scene', 'Whether the place itself is recognisable, even without buildings or a skyline'),
            ('plant', 'Distinctive vegetation and shorelines'),
            ('sun', 'Sun position and shadows'),
            ('glasses', 'Reflections in water, glasses or windows'),
            ('people', 'What other people post from the same trip'),
            ('clock', 'When you post'),
        ],
    },
    'cta': {
        'h2': 'Your spot stays yours.',
        'p': 'Eight Android apps, one for every hobby. Choose yours on Google Play.',
        'btn': 'Choose your app',
    },
    'footer': {
        'about': 'Photo privacy for the outdoors. Eight Android apps that check and protect your photos right on your phone.',
        'apps': 'SpotShield apps', 'more': 'More', 'policies': 'Privacy policies', 'contact': 'Contact',
        'copyright': '© 2026 Denis Korinsek', 'trademark': 'Android and Google Play are trademarks of Google LLC.',
    },
    'notfound': {'title': 'Page not found — SpotShield', 'h1': 'That page isn’t here.', 'p': 'The link may be old or mistyped.', 'btn': 'Back to SpotShield'},
}

SL = {
    'lang': 'sl', 'locale': 'sl_SI', 'other_lang': 'en', 'other_href': '../', 'other_label': 'English',
    'title': 'SpotShield — Pokaži trenutek. Ne razkrij kraja.',
    'description': 'Osem aplikacij za Android, ki najdejo in prekrijejo namige, ki izdajo tvoj spot – podatke GPS, table, registrske tablice, zaslone – kar na tvojem telefonu. Brez dovoljenja za internet, brez računa, brez analitike.',
    'nav': {
        'aria': 'Glavni meni', 'brand_aria': 'SpotShield, na vrh strani', 'apps': 'Aplikacije', 'how': 'Kako deluje', 'privacy': 'Zasebnost',
        'cta': 'Prenesi aplikacije', 'lang_aria': 'Jezik', 'menu': 'Meni',
        'theme_dark': 'Preklopi na svetli videz', 'theme_light': 'Preklopi na temni videz',
    },
    'hero': {
        'eyebrow': 'Osem aplikacij za Android · Zasebnost fotografij v naravi',
        'h1a': 'Pokaži trenutek.', 'h1b': 'Ne razkrij kraja.',
        'lede': 'Ena fotografija lahko izda tvoj spot – GPS v datoteki, tabla, registrska tablica, zaslon v ozadju. SpotShield te namige najde in jih prekrije, preden deliš. Za vsak hobi svoja aplikacija, vse na tvojem telefonu.',
        'picker': 'Izberi svoj hobi', 'picker_aria': 'Osem aplikacij SpotShield',
        'primary': 'Prenesi aplikacije', 'secondary': 'Poglej, kako deluje',
        'trust': 'Brez dovoljenja za internet · Brez računa · Brez analitike',
        'deck_aria': 'Osem aplikacij, ena za drugo',
    },
    'apps': {
        'eyebrow': 'Aplikacije · Android', 'h2': 'Osem aplikacij. Ena obljuba.',
        'lede': 'Vsaka aplikacija govori jezik svojega hobija – številke ribolovnih mest, table revirjev, preže in opazovalnice – in drži isto obljubo: kraj ostane tvoj.',
        'play': 'Google Play', 'play_aria': 'Prenesi {name} z Google Play', 'priv': 'Zasebnost', 'priv_aria': 'Pravilnik o zasebnosti za {name}',
        'items': {
            'carp':     dict(aud='Krapolovci',      kicker='Zasebnost za ribiče',           l1='Objavi ulov.',    l2='Ne razkrij spota.',     alt='Ribič ob mraku drži krapa ob ribniku'),
            'fly':      dict(aud='Muharji',         kicker='Zasebnost za muharje',          l1='Pokaži postrv.',  l2='Ne razkrij tolmuna.',   alt='Postrv v rokah nad bistro alpsko reko, v ozadju muhar'),
            'predator': dict(aud='Lovci roparic',   kicker='Zasebnost za lovce roparic',    l1='Objavi ščuko.',   l2='Ne razkrij spota.',     alt='Ščuka v rokah nad jezerom ob sončnem zahodu'),
            'sea':      dict(aud='Morski ribiči',   kicker='Zasebnost za morske ribiče',    l1='Pokaži ulov.',    l2='Ne razkrij pozicije.',  alt='Orada v rokah v sončni marini'),
            'hunter':   dict(aud='Lovci',           kicker='Zasebnost za lovce',            l1='Pokaži trofejo.', l2='Ne razkrij preže.',     alt='Jelen v lovišču ob zori, v ozadju preža'),
            'mushroom': dict(aud='Gobarji',         kicker='Zasebnost za gobarje',          l1='Pokaži jurčke.',  l2='Ne razkrij rastišča.',  alt='Košara jurčkov na gozdni poti'),
            'birder':   dict(aud='Opazovalci ptic', kicker='Zasebnost za opazovalce ptic',  l1='Pokaži ptico.',   l2='Ne razkrij gnezdišča.', alt='Vodomec na veji v rezervatu, obdanem s trstičjem'),
            'treasure': dict(aud='Detektoristi',    kicker='Zasebnost za iskalce',          l1='Pokaži najdbo.',  l2='Ne razkrij lokacije.',  alt='Kovanec v roki nad zorano njivo, ob njem detektor kovin'),
        },
    },
    'demo': {
        'eyebrow': 'Poglej, kako deluje', 'h2': 'Ena fotografija. Pet namigov. Nobenega več.',
        'lede': 'Povleci ročaj. Levo je izvirnik z vsem, kar je SpotShield Carp našel. Desno je zaščitena kopija, ki jo je naredil – na telefonu, v nekaj sekundah.',
        'before': 'Prej', 'after': 'Potem', 'gps': 'GPS v datoteki', 'ok': 'Podatki o lokaciji odstranjeni', 'hint': 'Povleci za primerjavo',
        'range_aria': 'Primerjaj izvirno fotografijo z zaščiteno kopijo',
        'alt_before': 'Izvirna fotografija ribiča ob mraku. SpotShield označi možno registrsko tablico, tablo z napisom, kodo QR, oznako ribolovnega mesta in zaslon GPS.',
        'alt_after': 'Zaščitena kopija: tablica in zaslon GPS sta prekrita, tabla in oznaka mesta sta zamegljeni, koda QR je pikselizirana, podatki o lokaciji pa so odstranjeni.',
        'found': [
            ('pin', 'Lokacija, shranjena v datoteki', 'Odstranjena'),
            ('plate', 'Registrska tablica na avtu', 'Prekrita'),
            ('screen', 'Zaslon GPS na daljincu čolnička', 'Prekrit'),
            ('sign', 'Tabla ribnika in oznaka mesta', 'Zamegljeni'),
            ('qr', 'Koda QR na vedru', 'Pikselizirana'),
        ],
        'note': 'Prekrij, pikseliziraj, zamegli ali zapolni – za vsako območje izbereš sam ali pa vsa tvegana zaščitiš z enim dotikom. Fotografija v galeriji ostane taka, kot je bila.',
    },
    'how': {
        'eyebrow': 'Kako deluje', 'h2': 'Preglej. Preveri. Zaščiti. Deli.',
        'lede': 'Od fotografije, na katero si ponosen, do kopije, ki jo lahko varno objaviš – vse na tvojem telefonu.',
        'steps': [
            ('Preglej', 'Izberi fotografijo, jo deli iz druge aplikacije ali posnemi s kamero SpotShield. Šest preverjanj teče na telefonu.', 'SpotShield Fly Fishing pregleduje fotografijo: opravljena so tri od šestih preverjanj'),
            ('Preveri', 'Poglej vse, kar bi lahko razkrilo kraj – od podatkov o lokaciji v datoteki do table daleč v ozadju.', 'Poročilo o tveganju v SpotShield Carp: 78 od 100, visoko tveganje'),
            ('Zaščiti', 'Vsako območje prekrij, pikseliziraj, zamegli ali zapolni – ali pa vsa tvegana zaščiti z enim dotikom. »Zapolni« območje obnovi iz okolice.', 'Ugotovitve v SpotShield Birder: za vsako območje izberi prekrivanje, pikselizacijo, zameglitev ali zapolnitev'),
            ('Deli', 'Dobiš novo kopijo brez podatkov o lokaciji, ki jo SpotShield pred deljenjem še enkrat preveri. Fotografija v galeriji ostane taka, kot je bila.', 'SpotShield Treasure: zaščitena kopija je pripravljena, vsa preverjanja so uspela'),
        ],
        'checks_title': 'Kaj SpotShield preveri',
        'checks': [
            ('pin', 'Podatki o lokaciji v datoteki'), ('sign', 'Table in napisi'), ('plate', 'Registrske tablice'),
            ('screen', 'Zasloni z zemljevidi in sonarji'), ('qr', 'Kode QR in črtne kode'), ('city', 'Stavbe in obrisi gora'),
            ('video', 'Skriti video v gibljivih fotografijah'),
        ],
    },
    'privacy': {
        'eyebrow': 'Zasebnost', 'h2': 'Fotografije nikoli ne zapustijo tvoje naprave.',
        'lede': 'Vsaka aplikacija fotografije preveri in zaščiti na tvojem telefonu, tudi brez povezave. Aplikacije nimajo dovoljenja za internet, zato se nič ne more naložiti – ne k nam, ne h komur koli.',
        'pillars': [
            ('offline', 'Brez dovoljenja za internet', 'Android aplikacijam ne dovoli na splet, zato se nič ne more naložiti.'),
            ('noaccount', 'Brez računa', 'Brez registracije, e-pošte in profila.'),
            ('noanalytics', 'Brez analitike, brez oglasov', 'Edini dovoljenji sta kamera in – za »Preveri izvirnik« – lokacija, zapisana v fotografiji. Obe sta neobvezni.'),
        ],
        'art_aria': 'Ilustracija: telefon s fotografijo je v ščitu; okoli njega se širijo valovi, oblak in oznaka na zemljevidu pa sta prečrtana.',
    },
    'limits': {
        'eyebrow': 'Iskreno o omejitvah', 'h2': 'Česa SpotShield ne vidi',
        'lede': 'Nekaterih namigov ne prepozna nobena aplikacija. Pred deljenjem jih preveri sam.',
        'items': [
            ('scene', 'Ali je sam kraj prepoznaven, tudi brez stavb ali obrisa gora'),
            ('plant', 'Značilno rastlinje in obale'),
            ('sun', 'Položaj sonca in sence'),
            ('glasses', 'Odseve v vodi, očalih ali oknih'),
            ('people', 'Kaj z istega izleta objavijo drugi'),
            ('clock', 'Kdaj objaviš'),
        ],
    },
    'cta': {
        'h2': 'Tvoj spot ostane tvoj.',
        'p': 'Osem aplikacij za Android, ena za vsak hobi. Izberi svojo v trgovini Google Play.',
        'btn': 'Izberi aplikacijo',
    },
    'footer': {
        'about': 'Zasebnost fotografij v naravi. Osem aplikacij za Android, ki fotografije preverijo in zaščitijo kar na tvojem telefonu.',
        'apps': 'Aplikacije SpotShield', 'more': 'Več', 'policies': 'Pravilniki o zasebnosti', 'contact': 'Kontakt',
        'copyright': '© 2026 Denis Korinsek', 'trademark': 'Android in Google Play sta blagovni znamki družbe Google LLC.',
    },
    'notfound': {'title': 'Strani ni — SpotShield', 'h1': 'Te strani ni tukaj.', 'p': 'Povezava je morda stara ali napačno vtipkana.', 'btn': 'Nazaj na SpotShield'},
}
