"""The pages "The texts on the map" (web/texts/, web/fr/texts/, web/sv/texts/) and their images.

Transcribed from the Basel scan. Conventions: long s printed as s; abbreviations expanded (q̃ = que,
a tilde = a following n or m, p̄ = par); the printer's struck e (an unpronounced e) printed as e; the
æ ligature written ae. Everything else as printed: spelling, accents (and their absence), u for v and
v for u, i for j, apostrophes and word division ("n'ya", "que lon"). Each translation (English, modern
French, Swedish) follows the original line by line, close to the text.
Images: web versions (1600 px webp) and the full-resolution crops (each under 1 MB) in web/public/texts/.
Usage: .venv/bin/python scripts/make_texts_page.py .
"""
import html, shutil, sys
from pathlib import Path
from PIL import Image

root = Path(sys.argv[1])
Image.MAX_IMAGE_PIXELS = None

# (crop box on the scan, file name)
PANELS = {"poem-1": (1050, 5950, 2800, 6900), "poem-2": (4500, 6700, 6300, 7450), "title": (6300, 6700, 8300, 7550)}

# (as printed, English, modern French, Swedish)
POEM_1 = [  # lower left panel, three columns of 26 lines
    ("Gentilz lecteurs amateurs d'escripture,", "Gentle readers who love the written word,",
     "Aimables lecteurs, amateurs d'écriture,", "Ädla läsare som älskar skriften,"),
    ("Ioyeulx espritz regardez la stature", "joyful minds, behold the stature,",
     "esprits joyeux, regardez la stature,", "glada sinnen, se här gestalten,"),
    ("Le bastiment & la fondation", "the building and the founding,",
     "la construction et la fondation,", "byggnaden och grundläggningen,"),
    ("L'accroissement & l'augmentation,", "the growth and the increase,",
     "l'accroissement et l'agrandissement,", "tillväxten och utvidgningen,"),
    ("Et la façon comment Paris la ville", "and the way in which the town of Paris",
     "et la manière dont la ville de Paris", "och hur staden Paris"),
    ("S'est augmentée en matiere ciuille:", "has grown in its civic life:",
     "s'est agrandie dans sa vie civile ;", "har vuxit som samhälle:"),
    ("Considerez la sienne antiquité", "consider its antiquity,",
     "considérez son antiquité,", "betänk dess ålder,"),
    ("Ou maintz cas sont de singularité.", "in which many things are remarkable.",
     "où bien des choses sont singulières.", "där mycket är märkvärdigt."),
    ("Regardez bien tous ces beaux edifices", "Look well at all these fine buildings,",
     "Regardez bien tous ces beaux édifices,", "Se noga på alla dessa sköna byggnader,"),
    ("Recongnoissez ses louenges propices", "recognise the praises it deserves,",
     "reconnaissez les louanges qu'elle mérite,", "erkänn det lov som tillkommer den,"),
    ("Ou on comprent sa valeur & noblesse", "in which its worth and nobility are found,",
     "où l'on voit sa valeur et sa noblesse,", "där man ser dess värde och adel,"),
    ("Son hault estat: sa doulce gentillesse,", "its high estate, its gentle grace,",
     "son haut rang, sa douce gentillesse,", "dess höga stånd, dess milda behag"),
    ("Et tous les biens qu'on peult en verité", "and all the good that can truly",
     "et tout le bien qu'on peut en vérité", "och allt gott som man i sanning"),
    ("Totallement dire d'vne cité.", "be said of a city.",
     "dire tout entier d'une cité.", "kan säga om en stad."),
    ("Noble cite & ville tant exquise", "Noble city and town so exquisite,",
     "Noble cité et ville si exquise,", "Ädla stad, så utsökt,"),
    ("Dicte Paris de toutes gens requise", "called Paris, sought out by all people,",
     "nommée Paris, recherchée de tous,", "kallad Paris, eftersökt av alla,"),
    ("Peult auoir loz & deseruir la gloire", "may have praise and deserve the glory",
     "peut recevoir l'éloge et mériter la gloire", "kan få pris och förtjäna äran"),
    ("De tout honneur pour l'antique memoire", "of every honour, for the ancient memory",
     "de tous les honneurs, pour l'antique mémoire", "av all heder, för det gamla minnet"),
    ("De son premier & noble instaurateur,", "of its first and noble founder,",
     "de son premier et noble fondateur,", "av dess förste och ädle grundare,"),
    ("S'il est ainsi que Paris fondateur", "whether Paris was its founder,",
     "s'il est vrai que Paris en fut le fondateur,", "vare sig det var Paris som grundade den"),
    ("Ou s'ainsi est qu'auec puissant arroy", "or whether, with a mighty host,",
     "ou s'il est vrai qu'avec une puissante troupe", "eller om, med en mäktig här,"),
    ("Herculez Grec ait faict fondation", "Hercules the Greek founded",
     "Hercule le Grec a fondé", "greken Herkules grundade"),
    ("De la cité par vne nation", "the city with a people",
     "la cité avec un peuple", "staden med ett folk"),
    ("De son pays, ou si la gent Troyenne", "of his own country, or whether the Trojan race",
     "de son pays, ou si la nation troyenne", "från hans eget land, eller om trojanernas släkt"),
    ("Ont, la cité dicte parisienne,", "made, built and brought into being",
     "a, la cité dite parisienne,", "har gjort, byggt och gett liv åt"),
    ("Faicte & bastie, & mise en son essence", "the city called Parisian.",
     "faite et bâtie, et fait naître.", "den stad som kallas parisisk."),
    ("Ceulx cy nommez de treshaulte excellence:", "Those named here were of the highest excellence",
     "Ceux que l'on vient de nommer, de très haute excellence,", "De som här nämnts var av högsta förträfflighet"),
    ("Furent iadis, & de noblesse antique,", "in times past, and of ancient nobility;",
     "furent jadis, et d'antique noblesse ;", "i forna tider, och av gammal adel;"),
    ("Mesmement ceulx de source Dardanique", "indeed those of the line of Dardanus",
     "et surtout ceux de la lignée de Dardanus", "framför allt de av Dardanos ätt"),
    ("Furent trespreux, & les plus anciens", "were most valiant, and the most ancient",
     "furent très preux, et les plus anciens", "var de tappraste och de äldsta"),
    ("Qui furent onc es pays Asiens.", "that ever were in the lands of Asia.",
     "qui furent jamais dans les pays d'Asie.", "som någonsin fanns i Asiens länder."),
    ("Paris aussi eust couronne royalle", "Paris too wore a royal crown",
     "Paris aussi porta la couronne royale", "Paris bar också kunglig krona"),
    ("Et fut le Roy de France la loyalle,", "and was king of loyal France,",
     "et fut roi de la loyale France ;", "och var kung i det trogna Frankrike;"),
    ("Dont si l'vn d'eulx la faicte & instaurée", "so if one of them made and founded it,",
     "si donc l'un d'eux l'a faite et fondée,", "om alltså en av dem byggde och grundade den,"),
    ("Estre ell' en doibt prisée & honorée,", "it ought to be prized and honoured for it.",
     "elle doit en être prisée et honorée.", "bör den prisas och äras för det."),
    ("Pareillement la sienne antiquité", "Its antiquity, likewise,",
     "De même, son antiquité", "Likaså går dess ålder"),
    ("Est de long temps, car à la verité", "goes back a long way, for in truth",
     "remonte loin, car en vérité,", "långt tillbaka, ty i sanning:"),
    ("Huyt cens trente ans auant que Dieu souffrit", "eight hundred and thirty years before God suffered",
     "huit cent trente ans avant que Dieu souffrît", "åttahundratrettio år innan Gud led"),
    ("Tresdure mort, & à la croix s'offrit", "a cruel death and offered himself on the cross,",
     "une mort très dure et s'offrît sur la croix,", "en mycket hård död och offrade sig på korset"),
    ("Paris auoit prins son commencement", "Paris had taken its beginning",
     "Paris avait pris son commencement", "hade Paris tagit sin början"),
    ("Par les Troyens, & le sien fondement.", "and its foundation from the Trojans.",
     "et sa fondation par les Troyens.", "och fått sin grund genom trojanerna."),
    ("Or est Paris en tres bel aer assise,", "Now Paris is set in very fine air;",
     "Or Paris est située en très bon air ;", "Nu ligger Paris i mycket god luft;"),
    ("Entour soy a la riuiere propice", "around it is the kindly river,",
     "elle a autour d'elle la rivière propice", "runt sig har den den gynnsamma floden,"),
    ("Et fleuue doulx que lon appelle Seine,", "the gentle stream called the Seine,",
     "et le doux fleuve que l'on appelle Seine,", "den milda ström som kallas Seine,"),
    ("Puis est remplie de tres belle fonteine:", "and it is full of very fine springs.",
     "et elle est pleine de très belles fontaines.", "och den är full av sköna källor."),
    ("De l'autre part sont les foretz trespleines", "Elsewhere are forests full",
     "D'autre part, il y a les forêts pleines", "Därtill finns skogar fulla"),
    ("De venaison, champaignes, boys, & plantes,", "of game, and fields, woods and plants,",
     "de gibier, les campagnes, les bois et les plantes,", "av vilt, och fält, lundar och växter,"),
    ("Terres portans les vignes tresplaisantes", "lands bearing most pleasant vines,",
     "des terres portant des vignes très plaisantes,", "jordar som bär de ljuvligaste vinrankor,"),
    ("Aultres aussy en tous bledz habondantes,", "others rich in every kind of grain.",
     "d'autres abondantes en toutes sortes de blés.", "andra rika på all slags säd."),
    ("Laer y est doulx, & la terre fertille", "The air is mild there, the soil fertile,",
     "L'air y est doux, et la terre fertile,", "Luften är mild där och jorden bördig,"),
    ("Et en tous fruictz trescommode & vtille.", "fit and useful for every kind of fruit.",
     "très propice et utile à tous les fruits.", "väl lämpad och nyttig för all slags frukt."),
    ("En elle aussi sont grans chasteaulx & tours", "In it too are great castles and towers,",
     "En elle aussi sont de grands châteaux et des tours,", "I den finns också stora slott och torn,"),
    ("Plus qu'il n'ya d'icy iusques à Tours.", "more than there are from here to Tours.",
     "plus qu'il n'y en a d'ici jusqu'à Tours.", "fler än det finns härifrån ända till Tours."),
    ("Maisons d'honneur on voit dedens Lutece", "In Lutetia one sees noble houses,",
     "On voit dans Lutèce de nobles demeures,", "I Lutetia ser man förnäma hus,"),
    ("Maint bastillon, & riche forteresse", "many a bastion and rich fortress,",
     "maint bastion et riche forteresse,", "mången bastion och rik fästning,"),
    ("Comme le Louure, & la Bastille noble", "like the Louvre and the noble Bastille,",
     "comme le Louvre et la noble Bastille,", "som Louvren och den ädla Bastiljen,"),
    ("Dont telle n'à dedens Constantinoble.", "whose like Constantinople has not.",
     "dont Constantinople n'a pas la pareille.", "vars like Konstantinopel inte har."),
    ("Puis des Seigneurs les maisons de plaisance", "Then the lords' houses of pleasure,",
     "Puis les maisons de plaisance des seigneurs,", "Sedan herrarnas lusthus,"),
    ("Les grans logis ou prennent ample aisance", "the great lodgings where they live in ample ease,",
     "les grands logis où ils vivent bien à l'aise,", "de stora gårdar där de lever i rik bekvämlighet,"),
    ("Comme l'hostel de Bourbon, Villeroy", "such as the Hôtel de Bourbon, Villeroy",
     "comme l'hôtel de Bourbon, Villeroy", "som Hôtel de Bourbon, Villeroy"),
    ("Dict chasteau pers, & la maison du Roy", "called the “château pers”, and the King's house",
     "dit « château pers », et la maison du roi", "kallat ”château pers”, och kungens hus"),
    ("Pres le palays, lequel palays à bruyt", "by the Palace, a palace renowned",
     "près du Palais, lequel Palais a la réputation", "vid Palatset, ett palats som har rykte om sig"),
    ("D'estre le mieulx en bel œuure construict", "as the finest and best-built work",
     "d'être l'ouvrage le plus beau et le mieux construit", "att vara det skönaste och bäst byggda verk"),
    ("Qu'on veit iamais en la chrestienté,", "ever seen in Christendom,",
     "qu'on ait jamais vu dans la chrétienté,", "som någonsin skådats i kristenheten,"),
    ("Pour sa grandeur, puis on voit à planté", "for its size; then one sees in plenty",
     "pour sa grandeur ; puis on voit à foison", "för sin storlek; sedan ser man i mängd"),
    ("D'aultres logis pleins de beaulx edifices", "other lodgings, full of fine buildings",
     "d'autres logis, pleins de beaux édifices", "andra gårdar, fulla av sköna byggnader"),
    ("Pour les bourgeoys & citoyens propices.", "fit for the burghers and citizens.",
     "qui conviennent aux bourgeois et aux citoyens.", "som passar borgare och stadsbor."),
    ("Ceste ville à quatorze portes close", "This town is closed by fourteen gates",
     "Cette ville est fermée de quatorze portes", "Denna stad är sluten med fjorton portar"),
    ("Et haultz rampars, qui n'est pas peu de chose", "and high ramparts, which is no small thing;",
     "et de hauts remparts, ce qui n'est pas peu de chose ;", "och höga vallar, vilket inte är lite;"),
    ("Profondz fossez tout alentour s'estendent", "deep ditches stretch all around,",
     "de profonds fossés s'étendent tout autour,", "djupa vallgravar sträcker sig runt om,"),
    ("Ou maintes eaues de toutes pars se rendent,", "into which many waters flow from every side.",
     "où maintes eaux se rendent de toutes parts.", "dit många vatten rinner från alla håll."),
    ("Puis apres sont cinq grans pontz pour passer", "Then there are five great bridges for crossing",
     "Puis il y a cinq grands ponts pour passer", "Sedan finns fem stora broar för att gå"),
    ("Par dessus l'eaue, aussy pour rapasser,", "over the water, and for crossing back,",
     "par-dessus l'eau, et aussi pour repasser,", "över vattnet, och för att gå tillbaka,"),
    ("De la Cité, en l'vniuersité", "from the Cité to the University.",
     "de la Cité à l'Université.", "från Cité till Universitetet."),
    ("Auec ce sont maintes eglises belles", "Besides, there are many fine churches,",
     "Avec cela il y a maintes belles églises,", "Därtill finns många sköna kyrkor,"),
    ("Temples diuins, monasteres, chappelles,", "holy temples, monasteries, chapels,",
     "temples divins, monastères, chapelles,", "heliga tempel, kloster, kapell,"),
    ("En tresgrand nombre, on peult pareillement", "in very great number. One may likewise",
     "en très grand nombre ; on peut pareillement", "i mycket stort antal. Man kan likaså"),
    ("Ceste louer pour le beau parlement.", "praise this city for its fine Parlement:",
     "louer celle-ci pour son beau Parlement :", "prisa denna stad för dess sköna Parlement:"),
]
POEM_2 = [  # lower middle panel, two columns of 15 lines: the poem goes on
    ("Le sainct senat ou sont les Conseilliers", "the holy senate, where the councillors sit,",
     "le saint sénat où siègent les conseillers,", "den heliga senaten, där rådsherrarna sitter,"),
    ("Nombre six vingtz hommes tressinguliers,", "six score men of great distinction",
     "au nombre de six vingts, hommes très remarquables,", "sex tjog män av stor förnämhet"),
    ("De grand sçauoir, qui tiennent leur office", "and great learning, who hold their office",
     "et de grand savoir, qui tiennent leur charge", "och stor lärdom, som har sitt ämbete"),
    ("De par le Roy, pour faire à tous iustice", "from the King, to do justice to all",
     "de par le roi, pour rendre justice à tous", "av kungen, för att skipa rätt åt alla"),
    ("Sur les proces à la court intimez", "in the suits brought before the court.",
     "dans les procès portés devant la cour.", "i de mål som dras inför domstolen."),
    ("Aultres gens sont en iustice estimez", "Other men are respected in justice,",
     "D'autres hommes sont estimés en justice,", "Andra män är aktade inom rättskipningen,"),
    ("Tenant le lieu du grant preuost royal", "standing in for the great royal Provost,",
     "tenant lieu du grand prévôt royal,", "och står i den store kunglige prevostens ställe"),
    ("Pour ordonner leur iugement loyal", "to give their loyal judgement",
     "pour rendre leur jugement loyal", "för att fälla sin redliga dom"),
    ("A toutes gens selon leur cause bonne", "to all, according to the merits of their cause.",
     "à tous, selon le bon droit de leur cause.", "åt alla, efter deras saks rätt."),
    ("Apres ya mainte docte personne", "Then there is many a learned person",
     "Ensuite, il y a maintes personnes doctes", "Sedan finns mången lärd person"),
    ("Estudiant aux loix pour ce establiz", "studying the laws, appointed to that end,",
     "qui étudient les lois, établies pour cela,", "som studerar lagarna, insatta för detta,"),
    ("Et de sçauoir sont tresfort ennobliz", "and greatly ennobled by knowledge.",
     "et que le savoir ennoblit grandement.", "och högt förädlade av kunskap."),
    ("Dedens Paris les sciences florissent", "Within Paris the sciences flourish,",
     "Dans Paris fleurissent les sciences", "I Paris blomstrar vetenskaperna"),
    ("Et gens sçauans en ce lieu resplandissent", "and learned men shine in this place",
     "et les savants resplendissent en ce lieu", "och lärda män lyser på denna plats"),
    ("Plus qu'en nul lieu, car Palas y octroye", "more than anywhere, for Pallas grants,",
     "plus qu'en nul autre, car Pallas y accorde,", "mer än någon annanstans, ty Pallas skänker,"),
    ("Autant ou plus qu'en Athenes ou Troye", "as much as or more than in Athens or Troy,",
     "autant ou plus qu'à Athènes ou à Troie,", "lika mycket eller mer än i Aten eller Troja,"),
    ("Le sien seiour: & les muses sçauantes", "her dwelling here; and the learned Muses",
     "son séjour ; et les Muses savantes", "sin boning här; och de lärda muserna"),
    ("Font en ce lieu leur demeure tenantes,", "make their lasting home in this place,",
     "font en ce lieu leur demeure durable,", "har sin fasta boning på denna plats,"),
    ("Plus que iamais ne furent sur le mond", "more than ever they did on the mount",
     "plus qu'elles ne le firent jamais sur le mont", "mer än de någonsin hade på berget"),
    ("De Aonias, ou par elle semond", "of Aonia, where in former days",
     "d'Aonie, où, appelé par elle,", "i Aonien, dit hon fordom"),
    ("Estoit iadis maint homme pour apprendre,", "she called many a man to learning.",
     "venait jadis maint homme pour apprendre.", "kallade mången man för att lära."),
    ("Artz & mestiers, apres nous fault comprendre,", "Arts and crafts, next, we must include,",
     "Les arts et métiers, ensuite, il nous faut les compter,", "Konster och hantverk måste vi sedan räkna in,"),
    ("Desquelz il vient tresgrande vtilité", "from which comes very great profit",
     "d'où vient un très grand profit", "av vilka kommer mycket stor nytta"),
    ("Au lieu susdict aussy tranquilité,", "to the said place, and peace as well.",
     "au lieu susdit, et aussi la tranquillité.", "till nämnda ort, och också lugn."),
    ("Semblablement marchans de toutes guises", "Likewise merchants of every kind",
     "Pareillement, des marchands de toutes sortes", "Likaså kommer köpmän av alla slag"),
    ("Viennent illec pour toutes marchandises", "come there to sell wares",
     "viennent là pour toutes marchandises", "dit för att sälja varor"),
    ("Distribuer, & tant de peuple abonde", "of every sort; and so many people throng",
     "distribuer ; et tant de peuple abonde", "av alla slag; och så mycket folk strömmar till"),
    ("En cestuy lieu qu'il n'ya peuple au monde", "to this place that there is no people in the world",
     "en ce lieu qu'il n'y a peuple au monde", "denna plats att det inte finns något folk i världen"),
    ("Qui soit autant à chascun gratieuse", "so gracious to everyone",
     "qui soit aussi gracieux envers chacun", "som är så vänligt mot var och en"),
    ("Qu'est ceste cy, ny autant spatieuse.", "as this one, nor so spacious.",
     "que celle-ci, ni aussi spacieux.", "som detta, och inget så rymligt."),
]
TITLE = [
    ("Icy est le vray pourtraict naturel de la ville, cité, vniuersité & Faubourgz de Paris, ou sont "
     "iustement figurées toutes les Rues & Ruelles correspondantes l'vne à l'autre, ainsi qui sont de "
     "present situées, qui sont en nombre deux cens quatre vingtz & sept. Pareillement sont figurées "
     "toutes les Eglises, & Monasteres, qui sont en nombre cent quatre. Aussy sont figurez tous les "
     "Colleges, qui sont en nombre quarante neuf. Et pour congnoistre icelles Rues, Ruelles, Eglises, "
     "Monasteres & Colleges, vous trouuerrez leurs noms escriptz à chascun sur son propre endroict. "
     "Comme plus amplement vous pouez voir cy dessus.",
     "Here is the true portrait from life of the town, city, university and suburbs of Paris, in which "
     "all the streets and lanes are accurately drawn, each meeting the next as they now lie: two hundred "
     "and eighty-seven of them. Likewise all the churches and monasteries are drawn: one hundred and "
     "four. All the colleges are drawn too: forty-nine. And so that you may know these streets, lanes, "
     "churches, monasteries and colleges, you will find the name of each written in its own place, as "
     "you can see in full above.",
     "Voici le vrai portrait au naturel de la ville, de la cité, de l'université et des faubourgs de Paris, "
     "où sont exactement figurées toutes les rues et ruelles, chacune raccordée à l'autre, telles qu'elles "
     "sont situées à présent : elles sont au nombre de deux cent quatre-vingt-sept. Pareillement sont "
     "figurés toutes les églises et tous les monastères, au nombre de cent quatre. Sont aussi figurés tous "
     "les collèges, au nombre de quarante-neuf. Et pour reconnaître ces rues, ruelles, églises, monastères "
     "et collèges, vous trouverez le nom de chacun écrit à sa propre place, comme vous pouvez le voir plus "
     "amplement ci-dessus.",
     "Här är den sanna avbildningen efter naturen av staden, Cité, universitetet och förstäderna i Paris, "
     "där alla gator och gränder är riktigt tecknade, var och en ansluten till nästa, så som de nu ligger: "
     "tvåhundraåttiosju till antalet. Likaså är alla kyrkor och kloster tecknade: etthundrafyra till "
     "antalet. Alla kollegier är också tecknade: fyrtionio till antalet. Och för att ni ska känna igen dessa "
     "gator, gränder, kyrkor, kloster och kollegier finner ni vars och ens namn skrivet på dess egen plats, "
     "som ni kan se utförligare här ovan."),
    ("A Paris, par Oliuier Truschet, & Germain Hoyau, demourans en la Rue de Montorgueil, au Chef sainct Denys.",
     "At Paris, by Olivier Truschet and Germain Hoyau, living in the rue de Montorgueil, at the sign of the Head of Saint Denis.",
     "À Paris, par Olivier Truschet et Germain Hoyau, demeurant rue Montorgueil, à l'enseigne du Chef Saint-Denis.",
     "I Paris, av Olivier Truschet och Germain Hoyau, boende i rue Montorgueil, vid skylten Sankt Dionysius huvud."),
]

# ---------- words around the verse, per language ----------
L = {}
L["en"] = dict(
    path="/texts/", home="/", by="Paris 1550, by Peer Blekelj.",
    title="The texts on the map",
    desc="The poem in praise of Paris and the publishers' notice printed on the Truschet &amp; Hoyau plan of Paris, c. 1550, transcribed and translated into English line by line.",
    og_desc="A 108-line poem in praise of Paris and the publishers' notice, printed on the 1550 map: transcribed and translated.",
    lede="Below the city, the map carries a poem of 108 lines in praise of Paris, set in two framed panels, "
         "and a notice from its publishers. Here they are as printed, with an English translation line by line.",
    col_orig="As printed, c. 1550", col_tr="English",
    h_poem="A poem in praise of Paris",
    p_poem="The poem starts in the large panel at the lower left and carries on in the smaller panel in the "
           "middle, linked by the catchword “Le sainct” at the foot of the first. It is anonymous, in rhyming "
           "couplets of ten syllables. It runs through the city's legendary founding, its setting, its castles "
           "and great houses, its walls, bridges and churches, its courts, its university and its trade.",
    alt1="The first panel of the poem: three columns of verse in a framed cartouche",
    cap1="The first panel, lower left of the map (lines 1–78). Click for the full resolution.",
    alt2="The second panel of the poem: two columns of verse in a framed cartouche",
    cap2="The second panel, lower middle of the map (lines 79–108). Click for the full resolution.",
    h_notes="Notes",
    h_title="The publishers' notice",
    alt3="The title cartouche at the lower right of the map",
    cap3="The notice, lower right of the map. Click for the full resolution.",
    h_other="Other words on the map",
    h_about="About this transcription",
    h_sources="Sources",
    lang_links="Also in <a href=\"/fr/texts/\" hreflang=\"fr\" lang=\"fr\">français</a> · "
               "<a href=\"/sv/texts/\" hreflang=\"sv\" lang=\"sv\">svenska</a>",
)
L["fr"] = dict(
    path="/fr/texts/", home="/?lang=fr", by="Paris 1550, par Peer Blekelj.",
    title="Les textes du plan",
    desc="Le poème à la louange de Paris et l'avis des éditeurs imprimés sur le plan de Truschet et Hoyau, vers 1550 : transcription et version en français moderne, vers par vers.",
    og_desc="Un poème de 108 vers à la louange de Paris et l'avis des éditeurs, imprimés sur le plan de 1550 : transcription et français moderne.",
    lede="Sous la ville, le plan porte un poème de 108 vers à la louange de Paris, réparti dans deux cartouches, "
         "et un avis de ses éditeurs. Les voici tels qu'imprimés, avec une version en français moderne, vers par vers.",
    col_orig="Tel qu'imprimé, vers 1550", col_tr="Français moderne",
    h_poem="Un poème à la louange de Paris",
    p_poem="Le poème commence dans le grand cartouche en bas à gauche et se poursuit dans le plus petit, au "
           "milieu, relié par la réclame « Le sainct » au pied du premier. Il est anonyme, en décasyllabes à rimes "
           "plates. Il passe en revue la fondation légendaire de la ville, son site, ses châteaux et ses grands "
           "hôtels, ses murs, ses ponts et ses églises, ses cours de justice, son université et son commerce.",
    alt1="Le premier cartouche du poème : trois colonnes de vers dans un cadre",
    cap1="Le premier cartouche, en bas à gauche du plan (vers 1–78). Cliquez pour la pleine résolution.",
    alt2="Le second cartouche du poème : deux colonnes de vers dans un cadre",
    cap2="Le second cartouche, en bas au milieu du plan (vers 79–108). Cliquez pour la pleine résolution.",
    h_notes="Notes",
    h_title="L'avis des éditeurs",
    alt3="Le cartouche du titre, en bas à droite du plan",
    cap3="L'avis, en bas à droite du plan. Cliquez pour la pleine résolution.",
    h_other="Autres inscriptions du plan",
    h_about="À propos de cette transcription",
    h_sources="Sources",
    lang_links="Aussi en <a href=\"/texts/\" hreflang=\"en\" lang=\"en\">English</a> · "
               "<a href=\"/sv/texts/\" hreflang=\"sv\" lang=\"sv\">svenska</a>",
)
L["sv"] = dict(
    path="/sv/texts/", home="/?lang=sv", by="Paris 1550, av Peer Blekelj.",
    title="Texterna på kartan",
    desc="Dikten till Paris lov och utgivarnas meddelande, tryckta på Truschets och Hoyaus Parisplan från omkring 1550: avskrift och svensk översättning rad för rad.",
    og_desc="En dikt på 108 rader till Paris lov och utgivarnas meddelande, tryckta på kartan från 1550: avskrift och översättning.",
    lede="Nedanför staden bär kartan en dikt på 108 rader till Paris lov, fördelad på två inramade fält, och ett "
         "meddelande från utgivarna. Här står de som de trycktes, med en svensk översättning rad för rad.",
    col_orig="Som tryckt, ca 1550", col_tr="Svenska",
    h_poem="En dikt till Paris lov",
    p_poem="Dikten börjar i det stora fältet nere till vänster och fortsätter i det mindre i mitten; de binds "
           "samman av kustoden ”Le sainct” längst ned i det första. Den är anonym, skriven i rimmade par om tio "
           "stavelser. Den går igenom stadens legendariska grundande, dess läge, dess slott och stora palats, "
           "dess murar, broar och kyrkor, dess domstolar, dess universitet och dess handel.",
    alt1="Diktens första fält: tre spalter vers i en inramad kartusch",
    cap1="Det första fältet, nere till vänster på kartan (rad 1–78). Klicka för full upplösning.",
    alt2="Diktens andra fält: två spalter vers i en inramad kartusch",
    cap2="Det andra fältet, nere i mitten av kartan (rad 79–108). Klicka för full upplösning.",
    h_notes="Kommentarer",
    h_title="Utgivarnas meddelande",
    alt3="Titelkartuschen nere till höger på kartan",
    cap3="Meddelandet, nere till höger på kartan. Klicka för full upplösning.",
    h_other="Andra ord på kartan",
    h_about="Om avskriften",
    h_sources="Källor",
    lang_links="Även på <a href=\"/texts/\" hreflang=\"en\" lang=\"en\">English</a> · "
               "<a href=\"/fr/texts/\" hreflang=\"fr\" lang=\"fr\">français</a>",
)


def place(pid, text):
    return f'<a href="/place/{pid}/">{text}</a>'


BRIDGES = {
    "en": f"{place('L0002', 'Pont Notre-Dame')}, {place('L0004', 'Pont au Change')} and {place('L0005', 'Pont aux Meuniers')} "
          f"(a bridge of water mills) on the right arm of the Seine; {place('L0003', 'Petit-Pont')} and "
          f"{place('L0006', 'Pont Saint-Michel')} on the left arm",
    "fr": f"le {place('L0002', 'pont Notre-Dame')}, le {place('L0004', 'pont au Change')} et le {place('L0005', 'pont aux Meuniers')} "
          f"(un pont de moulins) sur le grand bras de la Seine ; le {place('L0003', 'Petit-Pont')} et le "
          f"{place('L0006', 'pont Saint-Michel')} sur le petit bras",
    "sv": f"{place('L0002', 'Pont Notre-Dame')}, {place('L0004', 'Pont au Change')} och {place('L0005', 'Pont aux Meuniers')} "
          f"(en bro med vattenkvarnar) över Seines norra arm; {place('L0003', 'Petit-Pont')} och "
          f"{place('L0006', 'Pont Saint-Michel')} över den södra",
}

NOTES_POEM = {
    "en": [
        "<b>Paris, Hercules, the Trojans (lines 19–41):</b> the poem weighs the founding legends of its day "
        "without choosing. In one, Paris was founded by Trojan exiles: in Jean Lemaire de Belges' "
        "<i>Illustrations de Gaule</i> (1510–1513), Hector's son, renamed Francus, founds it and names it after his "
        "uncle Paris. Another, from the forged <i>Antiquities</i> of Annius of Viterbo (1498), made Paris a king "
        "of the Gauls (lines 32–33); a third credited Hercules. Dardanus (line 29) was the ancestor of the kings "
        "of Troy. None of this has any historical basis: the city takes its name from the Parisii, the Gaulish "
        "people who lived there.",
        "<b>“Eight hundred and thirty years before God suffered”</b> (line 38): about 800 BC by the legend's "
        "reckoning.",
        "<b>Two lines without a partner:</b> the poem rhymes in couplets, but lines 21 (<i>arroy</i>) and 74 "
        "(<i>vniuersité</i>) have no rhyme; perhaps a line was dropped each time when the type was set. The "
        "count of 108 is of the lines as printed.",
        "<b>Lutetia</b> (line 54): the Roman name of Paris.",
        f"<b>The Hôtel de Bourbon</b> (line 60): the {place('L0030', 'Petit-Bourbon')}, beside the Louvre.",
        "<b>Villeroy, “château pers”</b> (lines 60–61): the words are clear on the scan, the meaning is not. "
        "Villeroy is probably the town house of the Neufville family, lords of Villeroy, in the rue des "
        "Bourdonnais, whose oldest parts go back to about 1370; rebuilt in the 17th century, it still stands. "
        "<i>Pers</i> was a blue or blue-grey colour; we have found no source that explains the name.",
        f"<b>The King's house by the Palace</b> (lines 61–62): the Palace is the {place('L0021', 'Palais de la Cité')}, "
        "the old royal palace on the island, by then above all the seat of the Parlement (today's Palais de "
        "Justice). Which royal house beside it the poet means is not clear.",
        f"<b>Five great bridges</b> (line 72): {BRIDGES['en']}. All five are on the map.",
        "<b>The holy senate</b> (lines 78–83): the Parlement of Paris, the highest court of the realm, not an "
        "assembly. Francis I (r. 1515–1547) enlarged it with two new chambers of twenty members each and a score "
        "more judges; “six score” (120) councillors around 1550 is plausible, but we have not been able to "
        "confirm the exact figure.",
        "<b>Standing in for the Provost</b> (lines 84–87): <i>tenant le lieu</i>, “holding the place”, is what "
        "<i>lieutenant</i> means. The Prévôt de Paris was the king's judge for the city; his lieutenants, civil "
        "and criminal, did the judging in his name at the Grand Châtelet.",
        "<b>Pallas, the Muses, Aonia</b> (lines 93–99): Pallas Athena, goddess of wisdom; the Muses lived on "
        "Mount Helicon in Aonia, a poetic name for Boeotia in Greece. The claim: Paris and its university "
        "outshine Athens.",
    ],
    "fr": [
        "<b>Paris, Hercule, les Troyens (vers 19–41) :</b> le poème passe en revue les légendes de fondation de "
        "son temps sans trancher. Dans l'une, Paris est fondée par des Troyens exilés : dans les "
        "<i>Illustrations de Gaule</i> de Jean Lemaire de Belges (1510–1513), le fils d'Hector, devenu Francus, la "
        "fonde et lui donne le nom de son oncle Pâris. Une autre, tirée des fausses <i>Antiquités</i> d'Annius de "
        "Viterbe (1498), fait de Paris un roi des Gaules (vers 32–33) ; une troisième attribue la fondation à "
        "Hercule. Dardanus (vers 29) est l'ancêtre des rois de Troie. Rien de cela n'a de fondement historique : "
        "la ville tient son nom des Parisii, le peuple gaulois qui l'habitait.",
        "<b>« Huit cent trente ans avant que Dieu souffrît »</b> (vers 38) : vers 800 av. J.-C. selon le comput "
        "de la légende.",
        "<b>Deux vers sans rime :</b> le poème est en rimes plates, mais les vers 21 (<i>arroy</i>) et 74 "
        "(<i>vniuersité</i>) n'ont pas de vers qui leur réponde ; peut-être un vers a-t-il chaque fois été omis "
        "à la composition. Le compte de 108 vers est celui de l'imprimé.",
        "<b>Lutèce</b> (vers 54) : le nom romain de Paris.",
        f"<b>L'hôtel de Bourbon</b> (vers 60) : le {place('L0030', 'Petit-Bourbon')}, à côté du Louvre.",
        "<b>Villeroy, « château pers »</b> (vers 60–61) : les mots sont nets sur le scan, le sens ne l'est pas. "
        "Villeroy désigne sans doute l'hôtel de la famille de Neufville, seigneurs de Villeroy, rue des "
        "Bourdonnais, dont les parties les plus anciennes remontent aux environs de 1370 ; reconstruit au "
        "XVIIe siècle, il existe toujours. <i>Pers</i> désignait une couleur bleue ou gris-bleu ; nous n'avons "
        "trouvé aucune source qui explique le nom.",
        f"<b>La maison du roi près du Palais</b> (vers 61–62) : le Palais est le {place('L0021', 'palais de la Cité')}, "
        "l'ancien palais royal de l'île, devenu surtout le siège du Parlement (l'actuel Palais de justice). "
        "On ne sait pas quelle maison royale voisine le poète désigne.",
        f"<b>Cinq grands ponts</b> (vers 72) : {BRIDGES['fr']}. Les cinq figurent sur le plan.",
        "<b>Le saint sénat</b> (vers 78–83) : le Parlement de Paris, la plus haute cour de justice du royaume, et "
        "non une assemblée. François Ier (1515–1547) l'agrandit de deux chambres nouvelles de vingt membres "
        "chacune et d'une vingtaine de juges de plus ; « six vingts » (120) conseillers vers 1550 est plausible, "
        "mais nous n'avons pas pu vérifier le chiffre exact.",
        "<b>Tenant lieu du prévôt</b> (vers 84–87) : <i>tenant le lieu</i>, c'est le sens même de "
        "<i>lieutenant</i>. Le prévôt de Paris était le juge du roi pour la ville ; ses lieutenants, civil et "
        "criminel, jugeaient en son nom au Grand Châtelet.",
        "<b>Pallas, les Muses, l'Aonie</b> (vers 93–99) : Pallas Athéna, déesse de la sagesse ; les Muses "
        "habitaient l'Hélicon, en Aonie, nom poétique de la Béotie. L'idée : Paris et son université "
        "surpassent Athènes.",
    ],
    "sv": [
        "<b>Paris, Herkules, trojanerna (rad 19–41):</b> dikten väger sin tids legender om stadens grundande mot "
        "varandra utan att välja. Enligt en grundades Paris av landsflyktiga trojaner: i Jean Lemaire de Belges "
        "<i>Illustrations de Gaule</i> (1510–1513) grundar Hektors son, under namnet Francus, staden och "
        "uppkallar den efter sin farbror Paris. En annan, från Annius av Viterbos förfalskade <i>Antiquitates</i> "
        "(1498), gjorde Paris till en gallisk kung (rad 32–33); en tredje tillskrev Herkules grundandet. "
        "Dardanos (rad 29) var stamfar till Trojas kungar. Inget av detta har någon historisk grund: staden har "
        "sitt namn efter parisierna, det galliska folk som bodde där.",
        "<b>”Åttahundratrettio år innan Gud led”</b> (rad 38): omkring 800 f.Kr. enligt legendens tideräkning.",
        "<b>Två rader utan rim:</b> dikten rimmar parvis, men rad 21 (<i>arroy</i>) och 74 (<i>vniuersité</i>) "
        "saknar rimpartner; kanske föll en rad bort vid sättningen båda gångerna. Antalet 108 gäller raderna "
        "som de trycktes.",
        "<b>Lutetia</b> (rad 54): det romerska namnet på Paris.",
        f"<b>Hôtel de Bourbon</b> (rad 60): {place('L0030', 'Petit-Bourbon')}, intill Louvren.",
        "<b>Villeroy, ”château pers”</b> (rad 60–61): orden är tydliga på skanningen, betydelsen är det inte. "
        "Villeroy är troligen familjen Neufvilles stadspalats (herrarna till Villeroy) i rue des Bourdonnais, "
        "vars äldsta delar går tillbaka till omkring 1370; det byggdes om på 1600-talet och står kvar. "
        "<i>Pers</i> var en blå eller blågrå färg; vi har inte hittat någon källa som förklarar namnet.",
        f"<b>Kungens hus vid Palatset</b> (rad 61–62): Palatset är {place('L0021', 'Palais de la Cité')}, det gamla "
        "kungliga palatset på ön, som då framför allt var säte för Parlement (i dag Palais de Justice). Vilket "
        "kungligt hus intill det som avses är oklart.",
        f"<b>Fem stora broar</b> (rad 72): {BRIDGES['sv']}. Alla fem finns på kartan.",
        "<b>Den heliga senaten</b> (rad 78–83): Parlement de Paris, rikets högsta domstol, inte en folkförsamling. "
        "Frans I (regent 1515–1547) utökade den med två nya kammare om tjugo ledamöter vardera och ett tjugotal "
        "domare till; ”sex tjog” (120) rådsherrar omkring 1550 är rimligt, men vi har inte kunnat bekräfta "
        "den exakta siffran.",
        "<b>I prevostens ställe</b> (rad 84–87): <i>tenant le lieu</i>, ”som håller platsen”, är just vad "
        "<i>lieutenant</i> betyder. Prévôt de Paris var kungens domare för staden; hans ställföreträdare för "
        "civila mål och för brottmål dömde i hans namn på Grand Châtelet.",
        "<b>Pallas, muserna, Aonien</b> (rad 93–99): Pallas Athena, visdomens gudinna; muserna bodde på berget "
        "Helikon i Aonien, ett poetiskt namn för Boiotien i Grekland. Tanken: Paris och dess universitet "
        "överglänser Aten.",
    ],
}

NOTES_TITLE = {
    "en": [
        "<b>The counts:</b> the notice promises 287 streets and lanes, 104 churches and monasteries and 49 "
        "colleges. The labels read for this site name 219 streets, 91 churches and religious houses and 32 "
        "colleges; many more are drawn without a name (see <a href=\"/method/#labels\">how the labels were "
        "read</a>).",
        "<b>The publishers:</b> the notice does not say who drew the city and who cut the woodblocks, and modern "
        "sources disagree. Both men belonged to the image-makers of the rue Montorgueil, who made large "
        "woodcut prints for hanging on walls: Truschet is recorded there in the 1550s as a cutter of pictures "
        "(<i>tailleur d'histoires</i>), at the sign of the Chef Saint-Denis; Hoyau later bought shares of a "
        "house nearby, the Bon Pasteur (1563 and 1566).",
        "<b>The Chef Saint-Denis</b> (the head of Saint Denis) was a house sign. Denis, first bishop of Paris, "
        "was beheaded on Montmartre and, in the legend, walked away carrying his head.",
        "<b>The date:</b> the notice gives none. Jules Cousin, who published the first facsimile in the 1870s, "
        "dated the plan about 1552; others say 1553. This site says c. 1550.",
    ],
    "fr": [
        "<b>Les nombres :</b> l'avis annonce 287 rues et ruelles, 104 églises et monastères et 49 collèges. Les "
        "inscriptions relevées pour ce site nomment 219 rues, 91 églises et maisons religieuses et 32 collèges ; "
        "beaucoup d'autres sont dessinés sans nom (voir <a href=\"/method/#labels\">la lecture des "
        "inscriptions</a>, en anglais).",
        "<b>Les éditeurs :</b> l'avis ne dit pas qui a dessiné la ville et qui a taillé les bois, et les sources "
        "modernes ne s'accordent pas. Tous deux appartenaient aux imagiers de la rue Montorgueil, qui "
        "produisaient de grandes estampes sur bois destinées à être accrochées au mur : Truschet y est attesté "
        "dans les années 1550 comme <i>tailleur d'histoires</i>, à l'enseigne du Chef Saint-Denis ; Hoyau "
        "achète plus tard des parts d'une maison voisine, le Bon Pasteur (1563 et 1566).",
        "<b>Le Chef Saint-Denis</b> était une enseigne de maison. Denis, premier évêque de Paris, fut décapité "
        "à Montmartre et, selon la légende, s'en alla en portant sa tête.",
        "<b>La date :</b> l'avis n'en donne aucune. Jules Cousin, qui en publia le premier fac-similé dans les "
        "années 1870, datait le plan d'environ 1552 ; d'autres disent 1553. Ce site dit « vers 1550 ».",
    ],
    "sv": [
        "<b>Siffrorna:</b> meddelandet utlovar 287 gator och gränder, 104 kyrkor och kloster och 49 kollegier. "
        "Namnen som lästs för den här webbplatsen gäller 219 gator, 91 kyrkor och klosterbyggnader och 32 "
        "kollegier; många fler är tecknade utan namn (se <a href=\"/method/#labels\">hur namnen lästes</a>, på "
        "engelska).",
        "<b>Utgivarna:</b> meddelandet säger inte vem som tecknade staden och vem som skar träblocken, och "
        "moderna källor är oense. Båda hörde till bildmakarna i rue Montorgueil, som tillverkade stora träsnitt "
        "att hänga på väggen: Truschet nämns där på 1550-talet som bildsnidare (<i>tailleur d'histoires</i>), "
        "vid skylten Chef Saint-Denis; Hoyau köpte senare andelar i ett hus i närheten, Bon Pasteur (1563 och "
        "1566).",
        "<b>Chef Saint-Denis</b> (Sankt Dionysius huvud) var en husskylt. Dionysius, Paris förste biskop, "
        "halshöggs på Montmartre och gick enligt legenden därifrån med sitt huvud i händerna.",
        "<b>Dateringen:</b> meddelandet anger ingen. Jules Cousin, som gav ut det första faksimilet på "
        "1870-talet, daterade planen till omkring 1552; andra säger 1553. Den här webbplatsen säger ca 1550.",
    ],
}

OTHER = {
    "en": [
        "<b>The title banner</b> at the top: <i lang=\"fr\">La ville, cité, université de Paris</i>, “the town, "
        "the city and the university of Paris”: the three parts of Paris at the time, the Ville on the right "
        "bank, the Cité on the island, the Université on the left bank.",
        "<b>The winds and the quarters:</b> blowing heads in three corners and Latin names along the edges: "
        "<i>Subsolanus</i> (the east wind) at the top left, <i>Oriens</i> (east) at the top, <i>Auster</i> (the "
        "south wind) at the top right; <i>Septentriones</i> (north) at the bottom left, <i>Occidens</i> (west) "
        "at the bottom and <i>Favonius</i> (the west wind) at the bottom right. The map is printed with east "
        "at the top.",
        "<b>The arms and the crescents</b> at the top: the arms of France (golden lilies on blue, under a "
        "crown), the arms of Paris (the ship), and between France and the Subsolanus three interlaced "
        "crescents, the emblem of King Henri II (r. 1547–1559).",
        "<b>BIBL. PUBL. BASILIENSIS</b>, bottom left: the stamp of the public library of Basel. Its copy is the "
        "only one known; the librarian Louis Sieber recognised it in 1874.",
    ],
    "fr": [
        "<b>La banderole du titre</b>, en haut : <i>La ville, cité, université de Paris</i>, les trois parties de "
        "Paris à l'époque : la Ville sur la rive droite, la Cité dans l'île, l'Université sur la rive gauche.",
        "<b>Les vents et les points cardinaux :</b> des têtes soufflant dans trois coins et des noms latins le "
        "long des bords : <i>Subsolanus</i> (le vent d'est) en haut à gauche, <i>Oriens</i> (l'est) en haut, "
        "<i>Auster</i> (le vent du sud) en haut à droite ; <i>Septentriones</i> (le nord) en bas à gauche, "
        "<i>Occidens</i> (l'ouest) en bas et <i>Favonius</i> (le vent d'ouest) en bas à droite. Le plan est "
        "imprimé l'est en haut.",
        "<b>Les armes et les croissants</b>, en haut : les armes de France (fleurs de lis d'or sur azur, sous une "
        "couronne), les armes de Paris (la nef) et, entre les armes de France et le Subsolanus, trois croissants "
        "entrelacés, l'emblème du roi Henri II (1547–1559).",
        "<b>BIBL. PUBL. BASILIENSIS</b>, en bas à gauche : le cachet de la bibliothèque publique de Bâle. Son "
        "exemplaire est le seul connu ; le bibliothécaire Louis Sieber l'a identifié en 1874.",
    ],
    "sv": [
        "<b>Titelbandet</b> överst: <i lang=\"fr\">La ville, cité, université de Paris</i>, ”staden, Cité och "
        "universitetet i Paris”: stadens tre delar på den tiden, Ville på högra stranden, Cité på ön och "
        "Université på vänstra stranden.",
        "<b>Vindarna och väderstrecken:</b> blåsande huvuden i tre hörn och latinska namn längs kanterna: "
        "<i>Subsolanus</i> (östanvinden) uppe till vänster, <i>Oriens</i> (öster) överst, <i>Auster</i> "
        "(sunnanvinden) uppe till höger; <i>Septentriones</i> (norr) nere till vänster, <i>Occidens</i> (väster) "
        "nederst och <i>Favonius</i> (västanvinden) nere till höger. Kartan är tryckt med öster uppåt.",
        "<b>Vapnen och halvmånarna</b> överst: Frankrikes vapen (gyllene liljor på blått under en krona), Paris "
        "vapen (skeppet) och, mellan Frankrikes vapen och Subsolanus, tre sammanflätade halvmånar, kung Henrik "
        "II:s emblem (regent 1547–1559).",
        "<b>BIBL. PUBL. BASILIENSIS</b>, nere till vänster: stämpeln från det offentliga biblioteket i Basel. "
        "Dess exemplar är det enda kända; bibliotekarien Louis Sieber identifierade det 1874.",
    ],
}

ABOUT = {
    "en": [
        "Transcribed from the Basel copy and checked line by line against the scan. The long s (ſ) is printed "
        "as s, the æ ligature as ae, and the printer's abbreviations are written out (<i>q̃</i> = <i>que</i>, "
        "<i>p̄lemẽt</i> = <i>parlement</i>, a tilde for a following n or m). Everything else is as printed: "
        "spelling, accents and their absence (<i>cite</i>, line 15), <i>u</i> for <i>v</i> and <i>v</i> for "
        "<i>u</i>, <i>i</i> for <i>j</i>, and word division (<i>n'ya</i>, <i>que lon</i>).",
        "The translation follows the original line by line where the syntax allows, so a sentence sometimes "
        "runs across lines in a different order. The transcription and translation were made with "
        "<a href=\"https://claude.com/claude-code\">Claude Code</a> (see <a href=\"/method/#built\">how this was "
        "built</a>); corrections are welcome.",
    ],
    "fr": [
        "Transcrit d'après l'exemplaire de Bâle et vérifié vers par vers sur le scan. Le s long (ſ) est rendu "
        "par s, la ligature æ par ae, et les abréviations de l'imprimeur sont développées (<i>q̃</i> = "
        "<i>que</i>, <i>p̄lemẽt</i> = <i>parlement</i>, le tilde pour un n ou un m). Tout le reste est conservé : "
        "graphie, accents et leur absence (<i>cite</i>, vers 15), <i>u</i> pour <i>v</i> et <i>v</i> pour "
        "<i>u</i>, <i>i</i> pour <i>j</i>, et coupure des mots (<i>n'ya</i>, <i>que lon</i>).",
        "La version moderne suit l'original vers par vers ; elle modernise la langue sans la paraphraser. La "
        "transcription et les traductions ont été faites avec <a href=\"https://claude.com/claude-code\">Claude "
        "Code</a> (voir <a href=\"/method/#built\">comment ce site a été fait</a>, en anglais) ; les corrections "
        "sont bienvenues.",
    ],
    "sv": [
        "Avskrivet efter exemplaret i Basel och kontrollerat rad för rad mot skanningen. Långt s (ſ) återges "
        "som s, ligaturen æ som ae, och tryckarens förkortningar är utskrivna (<i>q̃</i> = <i>que</i>, "
        "<i>p̄lemẽt</i> = <i>parlement</i>, tilde för ett följande n eller m). Allt annat står som det trycktes: "
        "stavning, accenter och deras frånvaro (<i>cite</i>, rad 15), <i>u</i> för <i>v</i> och <i>v</i> för "
        "<i>u</i>, <i>i</i> för <i>j</i>, och orddelning (<i>n'ya</i>, <i>que lon</i>).",
        "Översättningen följer originalet rad för rad där syntaxen tillåter, så en mening kan ibland löpa över "
        "raderna i annan ordning. Avskrift och översättningar är gjorda med <a "
        "href=\"https://claude.com/claude-code\">Claude Code</a> (se <a href=\"/method/#built\">hur webbplatsen "
        "byggdes</a>, på engelska); rättelser tas tacksamt emot.",
    ],
}

# The same list on every page: titles stay in their own language.
SOURCES = [
    "Jules Cousin, “Table des noms des rues… inscrits sur le plan de Paris publié vers 1552 par Olivier Truschet "
    "et Germain Hoyau”, <i>Mémoires de la Société de l'histoire de Paris et de l'Île-de-France</i>, t. I (1875), "
    "pp. 60–70: <a href=\"https://gallica.bnf.fr/ark:/12148/bpt6k6310467r/f68.item\">gallica.bnf.fr / BnF</a>.",
    "Catherine Hofmann, “Publishing and the Map Trade in France, 1470–1670”, in <i>The History of Cartography</i>, "
    "vol. 3 (University of Chicago Press, 2007), ch. 53: "
    "<a href=\"https://press.uchicago.edu/books/hoc/HOC_V3_Pt2/HOC_VOLUME3_Part2_chapter53.pdf\">PDF</a> "
    "(Truschet and Hoyau, the rue Montorgueil).",
    "Séverine Lepape, <i>Gravures de la rue Montorgueil</i> (Éditions de la BnF, 2015): "
    "<a href=\"https://books.openedition.org/editionsbnf/2341\">OpenEdition</a> (the Montorgueil image-makers; "
    "Hoyau and the Bon Pasteur house).",
    "<a href=\"https://fr.wikipedia.org/wiki/Plan_de_Truschet_et_Hoyau\">Plan de Truschet et Hoyau</a>, Wikipédia "
    "(the Basel copy, its rediscovery in 1874).",
    "<a href=\"https://en.wikipedia.org/wiki/Francus\">Francus</a>, Wikipedia; “The Reception of Annius of "
    "Viterbo's Forgeries: The <i>Antiquities</i> in Renaissance France”, "
    "<a href=\"https://www.journals.uchicago.edu/doi/10.1086/698141\">journals.uchicago.edu</a> (the founding "
    "legends).",
    "<a href=\"https://www.britannica.com/topic/history-of-France/France-1490-1715\">History of France, "
    "1490–1715</a>, Encyclopaedia Britannica (Francis I and the Parlement of Paris).",
    "<a href=\"https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Ch%C3%A2telet\">Châtelet</a>, "
    "Encyclopaedia Britannica, 1911 (the Prévôt and his lieutenants).",
    "<a href=\"https://en.wikipedia.org/wiki/H%C3%B4tel_de_Villeroy_(Paris,_1st_arrondissement)\">Hôtel de "
    "Villeroy (Paris, 1st arrondissement)</a>, Wikipedia.",
    "The bridges, the Palace and the Petit-Bourbon: their place pages on this site, with their own sources.",
]

# ---------- images ----------
# Full-resolution crops live in data/map_texts/ (committed, so the page can be rebuilt without the
# 98 MB scan); they are cut from the scan only when the scan is present. Each is under 1 MB, so the
# page links to the JPG itself.
crops = root / "data/map_texts"
out = root / "web/public/texts"
full = out / "full"
for d in (crops, out, full):
    d.mkdir(parents=True, exist_ok=True)
src = root / "source/basel.jpg"
scan = Image.open(src).convert("RGB") if src.exists() else None
size = {}
for name, box in PANELS.items():
    if scan is not None:
        scan.crop(box).save(crops / f"{name}.jpg", quality=92)
    shutil.copyfile(crops / f"{name}.jpg", full / f"{name}.jpg")
    im = Image.open(crops / f"{name}.jpg")
    im.thumbnail((1600, 1600))
    im.save(out / f"{name}.webp", quality=80)
    size[name] = im.size

# ---------- page ----------
e = html.escape
TR = {"en": 1, "fr": 2, "sv": 3}


def lines(rows, lg, start=1, cls="verse"):
    i_tr = TR[lg]
    head = (f'          <div class="ln head" aria-hidden="true"><span class="n"></span>'
            f'<span class="orig">{L[lg]["col_orig"]}</span><span class="tr">{L[lg]["col_tr"]}</span></div>')
    rows_html = "\n".join(
        f'          <div class="ln{' r5' if i % 5 == 0 else ''}" id="v{i}"><span class="n">{i if cls == "verse" else ""}</span>'
        f'<span class="orig" lang="fr">{e(r[0])}</span><span class="tr">{e(r[i_tr])}</span></div>'
        for i, r in enumerate(rows, start))
    return f'        <div class="{cls}">\n{head}\n{rows_html}\n        </div>'


def items(xs):
    return "\n".join(f"          <li>{x}</li>" for x in xs)


def figure(name, alt, cap):
    w, h = size[name]
    return (f'        <figure>\n          <a href="/texts/full/{name}.jpg"><img src="/texts/{name}.webp" '
            f'width="{w}" height="{h}" alt="{alt}" loading="lazy" /></a>\n'
            f'          <figcaption>{cap}</figcaption>\n        </figure>')


def page(lg):
    s = L[lg]
    return f"""<!doctype html>
<html lang="{lg}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{s['title']} · Paris 1550</title>
    <meta name="description" content="{s['desc']}" />
    <link rel="canonical" href="%SITE%{s['path']}" />
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="Paris 1550" />
    <meta property="og:title" content="{s['title']} · Paris 1550" />
    <meta property="og:description" content="{s['og_desc']}" />
    <meta property="og:url" content="%SITE%{s['path']}" />
    <meta property="og:image" content="%SITE%/og/site.jpg" />
    <meta property="og:image:width" content="800" />
    <meta property="og:image:height" content="420" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  </head>
  <body class="doc">
    <header class="doc-head">
      <a class="back" href="{s['home']}">← Paris 1550</a>
      <h1>{s['title']}</h1>
      <p class="lede">{s['lede']}</p>
      <p class="langs">{s['lang_links']}</p>
    </header>

    <main class="doc-body">
      <section id="poem">
        <h2>{s['h_poem']}</h2>
        <p>{s['p_poem']}</p>
{figure('poem-1', s['alt1'], s['cap1'])}
{lines(POEM_1, lg)}
{figure('poem-2', s['alt2'], s['cap2'])}
{lines(POEM_2, lg, len(POEM_1) + 1)}
        <h3>{s['h_notes']}</h3>
        <ul class="notes">
{items(NOTES_POEM[lg])}
        </ul>
      </section>

      <section id="notice">
        <h2>{s['h_title']}</h2>
{figure('title', s['alt3'], s['cap3'])}
{lines(TITLE, lg, cls="verse prose")}
        <h3>{s['h_notes']}</h3>
        <ul class="notes">
{items(NOTES_TITLE[lg])}
        </ul>
      </section>

      <section id="other">
        <h2>{s['h_other']}</h2>
        <ul class="notes">
{items(OTHER[lg])}
        </ul>
      </section>

      <section id="about-texts">
        <h2>{s['h_about']}</h2>
{chr(10).join(f'        <p>{p}</p>' for p in ABOUT[lg])}
      </section>

      <section id="sources">
        <h2>{s['h_sources']}</h2>
        <ul class="sources">
{items(SOURCES)}
        </ul>
        <p class="muted">{s['by']}</p>
      </section>
    </main>
    <script type="module" src="/src/method.ts"></script>
  </body>
</html>
"""


assert len(POEM_1) + len(POEM_2) == 108
for lg in L:
    dst = root / "web" / L[lg]["path"].strip("/") / "index.html"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(page(lg), encoding="utf-8")
    print(f"wrote {dst}")
