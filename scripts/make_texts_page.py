"""The page "The texts on the map" (web/texts/index.html) and its images (web/public/texts/).

Transcribed from the Basel scan: long s printed as s, abbreviations expanded (q̃ = que, a tilde
= a following n/m, p̄ = par), the printer's struck e (an unpronounced e) printed as e; spelling,
i/j and u/v otherwise as printed. English translation line by line, close to the original.
Usage: .venv/bin/python scripts/make_texts_page.py .
"""
import html, sys
from pathlib import Path
from PIL import Image

root = Path(sys.argv[1])
Image.MAX_IMAGE_PIXELS = None
SITE = "https://paris1550.vercel.app"

# (crop box on the scan, file name)
PANELS = {"poem-1": (1050, 5950, 2800, 6900), "poem-2": (4500, 6700, 6300, 7450), "title": (6300, 6700, 8300, 7550)}

POEM_1 = [  # lower left panel, three columns
    ("Gentilz lecteurs amateurs d'escripture,", "Gentle readers who love the written word,"),
    ("Ioyeulx espritz regardez la stature", "joyful minds, behold the stature,"),
    ("Le bastiment & la fondation", "the building and the founding,"),
    ("L'accroissement & l'augmentation,", "the growth and the increase,"),
    ("Et la façon comment Paris la ville", "and the way in which the town of Paris"),
    ("S'est augmentée en matiere ciuille:", "has grown as a city:"),
    ("Considerez la sienne antiquité", "consider its antiquity,"),
    ("Ou maintz cas sont de singularité.", "in which many things are remarkable."),
    ("Regardez bien tous ces beaux edifices", "Look well at all these fine buildings,"),
    ("Recongnoissez ses louenges propices", "recognise the praises it deserves,"),
    ("Ou on comprent sa valeur & noblesse", "in which its worth and nobility are found,"),
    ("Son hault estat: sa doulce gentillesse,", "its high estate, its gentle grace,"),
    ("Et tous les biens qu'on peult en verité", "and all the good that can truly"),
    ("Totallement dire d'une cité.", "be said of a city."),
    ("Noble cité & ville tant exquise", "Noble city and town so exquisite,"),
    ("Dicte Paris de toutes gens requise", "called Paris, sought out by all people,"),
    ("Peult auoir loz & deseruir la gloire", "may have praise and deserve the glory"),
    ("De tout honneur pour l'antique memoire", "of every honour, for the ancient memory"),
    ("De son premier & noble instaurateur,", "of its first and noble founder,"),
    ("S'il est ainsi que Paris fondateur", "whether Paris was its founder,"),
    ("Ou s'ainsi est qu'auec puissant arroy", "or whether, with a mighty host,"),
    ("Herculez Grec ait faict fondation", "Hercules the Greek founded"),
    ("De la cité par une nation", "the city with a people"),
    ("De son pays, ou si la gent Troyenne", "of his own country, or whether the Trojan race"),
    ("Ont, la cité dicte parisienne,", "made, built and brought into being"),
    ("Faicte & bastie, & mise en son essence", "the city called Parisian."),
    ("Ceulx cy nommez de treshaulte excellence:", "Those named here were of the highest excellence"),
    ("Furent iadis, & de noblesse antique,", "in times past, and of ancient nobility;"),
    ("Mesmement ceulx de source Dardanique", "indeed those of the line of Dardanus"),
    ("Furent trespreux, & les plus anciens", "were most valiant, and the most ancient"),
    ("Qui furent onc es pays Asiens.", "that ever were in the lands of Asia."),
    ("Paris aussi eust couronne royalle", "Paris too wore a royal crown"),
    ("Et fut le Roy de France la loyalle,", "and was king of loyal France,"),
    ("Dont si l'un d'eulx la faicte & instaurée", "so if one of them made and founded it,"),
    ("Estre ell' en doibt prisée & honorée,", "it ought to be prized and honoured for it."),
    ("Pareillement la sienne antiquité", "Its antiquity, likewise,"),
    ("Est de long temps, car à la verité", "goes back a long way, for in truth"),
    ("Huyt cens trente ans auant que Dieu souffrit", "eight hundred and thirty years before God suffered"),
    ("Tresdure mort, & à la croix s'offrit", "a cruel death and offered himself on the cross,"),
    ("Paris auoit prins son commencement", "Paris had taken its beginning"),
    ("Par les Troyens, & le sien fondement.", "and its foundation from the Trojans."),
    ("Or est Paris en tresbel aer assise,", "Now Paris is set in very fine air;"),
    ("Entour soy a la riuiere propice", "around it is the kindly river,"),
    ("Et fleuue doulx que l'on appelle Seine,", "the gentle stream called the Seine,"),
    ("Puis est remplie de tres belle fonteine:", "and it is full of very fine springs."),
    ("De l'autre part sont les foretz tresplaines", "Elsewhere are forests full"),
    ("De venaison, champaignes, boys, & plantes,", "of game, and fields, woods and plants,"),
    ("Terres portans les vignes tresplaisantes", "lands bearing most pleasant vines,"),
    ("Aultres aussy en tous bledz habondantes,", "others rich in every kind of grain."),
    ("L'aer y est doulx, & la terre fertille", "The air is mild there, the soil fertile,"),
    ("Et en tous fruictz trescommode & utille.", "fit and useful for every kind of fruit."),
    ("En elle aussi sont grans chasteaulx & tours", "In it too are great castles and towers,"),
    ("Plus qu'il n'y a d'icy iusques à Tours.", "more than there are from here to Tours."),
    ("Maisons d'honneur on voit dedens Lutece", "In Lutetia one sees noble houses,"),
    ("Maint bastillon, & riche forteresse", "many a bastion and rich fortress,"),
    ("Comme le Louure, & la Bastille noble", "like the Louvre and the noble Bastille,"),
    ("Dont telle n'a dedens Constantinoble.", "whose like Constantinople has not."),
    ("Puis des Seigneurs les maisons de plaisance", "Then the lords' houses of pleasure,"),
    ("Les grans logis ou prennent ample aisance", "the great lodgings where they live in ample ease,"),
    ("Comme l'hostel de Bourbon, Villeroy", "such as the Hôtel de Bourbon, Villeroy"),
    ("Dict chasteau pers, & la maison du Roy", "called the 'château pers', and the King's house"),
    ("Pres le palays, lequel palays a bruyt", "by the Palace, a palace renowned"),
    ("D'estre le mieulx en bel œuure construict", "as the finest and best-built work"),
    ("Qu'on veit iamais en la chrestienté,", "ever seen in Christendom,"),
    ("Pour sa grandeur, puis on voit à planté", "for its size; then one sees in plenty"),
    ("D'aultres logis pleins de beaulx edifices", "other lodgings, full of fine buildings"),
    ("Pour les bourgeoys & citoyens propices.", "fit for the burghers and citizens."),
    ("Ceste ville à quatorze portes close", "This town is closed by fourteen gates"),
    ("Et haultz rampars, qui n'est pas peu de chose", "and high ramparts, which is no small thing;"),
    ("Profondz fossez tout alentour s'estendent", "deep ditches stretch all around,"),
    ("Ou maintes eaues de toutes pars se rendent,", "into which many waters flow from every side."),
    ("Puis apres sont cinq grans pontz pour passer", "Then there are five great bridges for crossing"),
    ("Par dessus l'eaue, aussy pour rapasser,", "over the water, and for crossing back,"),
    ("De la Cité, en l'uniuersité", "from the Cité to the University."),
    ("Auec ce sont maintes eglises belles", "Besides, there are many fine churches,"),
    ("Temples diuins, monasteres, chappelles,", "holy temples, monasteries, chapels,"),
    ("En tresgrand nombre, on peult pareillement", "in very great number. One may likewise"),
    ("Ceste louer pour le beau parlement.", "praise this city for its fine Parlement:"),
]
POEM_2 = [  # lower middle panel, two columns: the poem goes on
    ("Le sainct senat ou sont les Conseilliers", "the holy senate, where the councillors sit,"),
    ("Nombre six vingtz hommes tressinguliers,", "six score men of great distinction"),
    ("De grand sçauoir, qui tiennent leur office", "and great learning, who hold their office"),
    ("De par le Roy, pour faire à tous iustice", "from the King, to do justice to all"),
    ("Sur les proces à la court intimez", "in the suits brought before the court."),
    ("Aultres gens sont en iustice estimez", "Other men are respected in justice,"),
    ("Tenant le lieu du grant preuost royal", "holding the court of the great royal Provost,"),
    ("Pour ordonner leur iugement loyal", "to give their loyal judgement"),
    ("A toutes gens selon leur cause bonne", "to all, according to the merits of their cause."),
    ("Apres y a mainte docte personne", "Then there is many a learned person"),
    ("Estudiant aux loix pour ce establiz", "studying the laws, appointed to that end,"),
    ("Et de sçauoir sont tresfort ennobliz", "and greatly ennobled by knowledge."),
    ("Dedens Paris les sciences florissent", "Within Paris the sciences flourish,"),
    ("Et gens sçauans en ce lieu resplandissent", "and learned men shine in this place"),
    ("Plus qu'en nul lieu, car Palas y octroye", "more than anywhere, for Pallas grants,"),
    ("Autant ou plus qu'en Athenes ou Troye", "as much as or more than in Athens or Troy,"),
    ("Le sien seiour: & les muses sçauantes", "her dwelling here; and the learned Muses"),
    ("Font en ce lieu leur demeure tenantes,", "make their lasting home in this place,"),
    ("Plus que iamais ne furent sur le mond", "more than ever they did on the mount"),
    ("De Aonias, ou par elle semond", "of Aonia, where in former days"),
    ("Estoit iadis maint homme pour apprendre,", "she called many a man to learning."),
    ("Artz & mestiers, apres nous fault comprendre,", "Arts and crafts, next, we must include,"),
    ("Desquelz il vient tresgrande utilité", "from which comes very great profit"),
    ("Au lieu susdict aussy tranquilité,", "to the said place, and peace as well."),
    ("Semblablement marchans de toutes guises", "Likewise merchants of every kind"),
    ("Viennent illec pour toutes marchandises", "come there to deal in every sort of ware,"),
    ("Distribuer, & tant de peuple abonde", "and so many people abound"),
    ("En cestuy lieu qu'il n'y a peuple au monde", "in this place that there is no people in the world"),
    ("Qui soit autant à chascun gratieuse", "so gracious to everyone"),
    ("Qu'est ceste cy, ny autant spatieuse.", "as this one, nor a city so spacious."),
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
     "you can see in full above."),
    ("A Paris, par Oliuier Truschet, & Germain Hoyau, demourans en la Rue de Montorgueil, au Chef sainct Denys.",
     "At Paris, by Olivier Truschet and Germain Hoyau, living in the rue Montorgueil, at the sign of the Head of Saint Denis."),
]

NOTES_POEM = [
    "<b>Paris, Hercules, the Trojans:</b> the poem weighs the three founding legends told in the Renaissance. "
    "The favourite made the city's founder a Trojan prince called Paris, from the line of Dardanus, Troy's ancestor; "
    "another credited Hercules. None has any historical basis.",
    "<b>“Eight hundred and thirty years before God suffered”:</b> that is, around 800 BC by the legend's reckoning.",
    "<b>Lutetia:</b> the Roman name of Paris.",
    "<b>Villeroy, “château pers”:</b> the line is hard to read with certainty; it seems to name the town house of the "
    "Neufville de Villeroy family. The meaning of “pers” (perhaps “blue-grey”, from its slate) is uncertain.",
    "<b>The King's house by the Palace:</b> the royal palace on the Île de la Cité, which by then housed the "
    "Parlement; the Sainte-Chapelle stands in its courtyard.",
    "<b>Five great bridges:</b> the Pont Notre-Dame, the Pont au Change and the Pont aux Meuniers on the right "
    "arm of the Seine, the Petit-Pont and the Pont Saint-Michel on the left: all on the map.",
    "<b>The holy senate:</b> the Parlement of Paris, the highest court of the realm. “Six score” (120) is about right "
    "for its councillors in the 1550s.",
    "<b>The great royal Provost:</b> the Prévôt de Paris, the king's judge, who sat at the Grand Châtelet.",
    "<b>Pallas, the Muses, Aonia:</b> Pallas Athena, goddess of wisdom; the Muses lived on Mount Helicon in Aonia "
    "(Boeotia). The claim: Paris and its university outshine Athens.",
]
NOTES_TITLE = [
    "<b>The counts:</b> the map names fewer streets, churches and colleges than it boasts; many are drawn but "
    "not labelled (see <a href=\"/method/#labels\">how the labels were read</a>).",
    "<b>The publishers:</b> Olivier Truschet was a printer and Germain Hoyau a woodcutter; nothing else is known "
    "of Hoyau. Their shop was in the rue Montorgueil, at a house with the sign of the head of Saint Denis.",
]

# ---------- images ----------
# Full-resolution crops live in data/map_texts/ (committed, so the page can be rebuilt without the
# 98 MB scan); they are cut from the scan only when the scan is present.
crops = root / "data/map_texts"
out = root / "web/public/texts"
crops.mkdir(parents=True, exist_ok=True)
out.mkdir(parents=True, exist_ok=True)
src = root / "source/basel.jpg"
scan = Image.open(src).convert("RGB") if src.exists() else None
for name, box in PANELS.items():
    if scan is not None:
        scan.crop(box).save(crops / f"{name}.jpg", quality=92)
    im = Image.open(crops / f"{name}.jpg")
    im.thumbnail((1600, 1600))
    im.save(out / f"{name}.webp", quality=80)

# ---------- page ----------
e = html.escape


def lines(rows, start=1):
    return "\n".join(
        f'          <div class="ln"><span class="n">{i}</span><span class="fr" lang="fr">{e(a)}</span><span class="en">{e(b)}</span></div>'
        for i, (a, b) in enumerate(rows, start))


def notes(items):
    return "\n".join(f"          <li>{n}</li>" for n in items)


page = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>The texts on the map · Paris 1550</title>
    <meta name="description" content="The verses and the title printed on the Truschet &amp; Hoyau plan of Paris, c. 1550, transcribed and translated into English line by line." />
    <link rel="canonical" href="{SITE}/texts/" />
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="Paris 1550" />
    <meta property="og:title" content="The texts on the map · Paris 1550" />
    <meta property="og:description" content="A poem in praise of Paris and the publishers' notice, printed on the 1550 map: transcribed and translated." />
    <meta property="og:url" content="{SITE}/texts/" />
    <meta property="og:image" content="{SITE}/og/site.jpg" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  </head>
  <body class="doc">
    <header class="doc-head">
      <a class="back" href="/">← Paris 1550</a>
      <h1>The texts on the map</h1>
      <p class="lede">Below the city, the map carries a poem of 108 lines in praise of Paris, set in two
        framed panels, and a notice from its publishers. Here they are as printed, with an English
        translation line by line.</p>
    </header>

    <main class="doc-body">
      <section id="poem">
        <h2>A poem in praise of Paris</h2>
        <p>The poem starts in the large panel at the lower left and carries on in the smaller panel in the
          middle, linked by the catchword “Le sainct” at the foot of the first. It is anonymous. It runs
          through the city's legendary founding, its setting, its castles and great houses, its walls,
          bridges and churches, its courts, its university and its trade.</p>
        <figure>
          <img src="/texts/poem-1.webp" width="1600" height="869" alt="The first panel of the poem: three columns of verse in a framed cartouche" loading="lazy" />
          <figcaption>The first panel, lower left of the map (lines 1–78).</figcaption>
        </figure>
        <div class="verse">
{lines(POEM_1)}
        </div>
        <figure>
          <img src="/texts/poem-2.webp" width="1600" height="667" alt="The second panel of the poem: two columns of verse in a framed cartouche" loading="lazy" />
          <figcaption>The second panel, lower middle of the map (lines 79–108).</figcaption>
        </figure>
        <div class="verse">
{lines(POEM_2, len(POEM_1) + 1)}
        </div>
        <h3>Notes</h3>
        <ul class="notes">
{notes(NOTES_POEM)}
        </ul>
      </section>

      <section id="title">
        <h2>The publishers' notice</h2>
        <figure>
          <img src="/texts/title.webp" width="1600" height="680" alt="The title cartouche at the lower right of the map" loading="lazy" />
          <figcaption>The title panel, lower right of the map.</figcaption>
        </figure>
        <div class="verse prose">
{lines(TITLE)}
        </div>
        <h3>Notes</h3>
        <ul class="notes">
{notes(NOTES_TITLE)}
        </ul>
      </section>

      <section id="other">
        <h2>Other words on the map</h2>
        <ul class="notes">
          <li><b>The title banner</b> at the top: <i lang="fr">La ville, cité, université de Paris</i>: “the
            town, the city and the university of Paris”, the three parts of Paris at the time: the Ville on
            the right bank, the Cité on the island, the Université on the left bank.</li>
          <li><b>The winds and the quarters:</b> blowing heads at the corners with Latin names:
            <i>Subsolanus</i> (the east wind) and <i>Oriens</i> (east) at the top, <i>Auster</i> (south),
            <i>Favonius</i> (the west wind) and <i>Occidens</i> (west) at the bottom, <i>Septentriones</i>
            (north) on the left. The map is printed with east at the top.</li>
          <li><b>The coats of arms</b> at the top: the arms of France (golden lilies on blue, under a crown)
            and the arms of Paris (the ship).</li>
          <li><b>BIBL. PUBL. BASILIENSIS</b>: the stamp of the public library of Basel, which holds the only
            known copy.</li>
        </ul>
      </section>

      <section id="about-texts">
        <h2>About this transcription</h2>
        <p>Transcribed from the Basel copy. The long s (ſ) is printed as s and the printer's abbreviations
          are written out; otherwise the spelling is kept as printed, including <i>u</i> for <i>v</i> and
          <i>i</i> for <i>j</i>. The translation follows the original line by line where the syntax allows,
          so a sentence sometimes runs across lines in a different order. The transcription and translation
          were made with <a href="https://claude.com/claude-code">Claude Code</a> (see
          <a href="/method/#built">how this was built</a>); corrections are welcome.</p>
        <p class="muted">Paris 1550, by Peer Blekelj.</p>
      </section>
    </main>
    <script type="module" src="/src/method.ts"></script>
  </body>
</html>
"""
dst = root / "web/texts/index.html"
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text(page, encoding="utf-8")
print(f"{len(POEM_1) + len(POEM_2)} lines of verse; wrote {dst}")
