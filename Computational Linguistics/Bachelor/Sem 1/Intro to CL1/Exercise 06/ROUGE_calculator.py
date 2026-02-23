
"""
This script calculates the ROUGE scores for a given translation.
ROUGE score has three different variants: ROUGE-1, ROUGE-2, and ROUGE-L.
Each of those variants will give you three different scores: precision, recall, and F-score.
Remember that F-scores are the harmonic mean of precision and recall.
So, we are only evaluating the F-score, since it combines the other two.

Below are short descriptions of the three variants of ROUGE,
as well as an interpretation guide for the F-SCORES of each ROUGE-variant.

ROUGE-1: Measures unigram (word-level) overlap.

- A ROUGE-1 score below 0.2 may indicate poor quality translations.
- A score between 0.2 and 0.4 suggests moderate quality.
- Scores above 0.4 indicate relatively good quality translations.


ROUGE-2: Measures bigram (phrase-level) overlap.

- A ROUGE-2 score below 0.1 may indicate poor quality translations.
- A score between 0.1 and 0.2 suggests moderate quality.
- Scores above 0.2 indicate relatively good quality translations.


ROUGE-L: Measures the longest common subsequence between the machine-generated and reference translations.

- A ROUGE-L score below 0.5 may indicate poor quality translations.
- A score between 0.5 and 0.7 suggests moderate quality.
- Scores above 0.7 indicate relatively good quality translations.
"""


# in the terminal, in the folder where you are running this script:
# Install rouge using the command: pip install rouge


from rouge import Rouge
rouge_calculator = Rouge()

# Which language are you evaluating for?
are_you_evaluating_for_the_source_lang = True

# open the right and set the text in there as the reference text
file = "Computational Linguistics/Intro to CL1/Exercise 06/source.txt" if are_you_evaluating_for_the_source_lang is True else "Computational Linguistics/Intro to CL1/Exercise 06/target.txt"
with open(file, 'r', encoding="utf-8") as f:
    reference_text = f.read()

# copy paste the text you want to evaluate here, i.e., the translation from the MT system you used
# Use a multi-line string
# Note: The texts you are comparing have to be the same language, otherwise, you did something wrong

text_to_be_evaluated = """In der eTravel World in Halle 7.1c zeigen namhafte Unternehmen sowie neue Start-ups ihre neuesten Apps und Innovationen für die Bereiche mobile Reisedienstleistungen und Social Media. Der Mann, der den Rechtshütern solche strategischen Anstrengungen und Überstunden abverlangte, war Hans-Ruedi Jaggi. Dieses Apartment befindet sich im Obergeschoss und bietet Aussicht auf die Prager Burg. Schwarzes, verstärktes Polyamid, Magnet-Anhänger-Set für 2 Mini-DIN-Kameras. Sprühen Sie das Abwehrmittel gleichmäßig auf den Bereich Ihres Schuhs. [ ... ] und die wachsende Zahl von Kooperationen [...] PDL), Portugal Das Beste von Puerto Rico Klicken Sie hier, um weitere Unterkünfte in der Nähe beliebter Sehenswürdigkeiten in Puerto Rico zu sehen. Beim Mikrowellenaufschluss wird die Probe mit einer Säuremischung in einem mikrowellentransparenten Druckgefäß auf bis zu 260 °C erhitzt. Diese Etappe ist 32,8 km lang und kann in 8 Stunden und 30 Minuten bewältigt werden. Kommentar Sebulon hat am 16.10.2013 um 00:04:10 UTC einen Kommentar veröffentlicht. Klicken Sie einfach auf das „T“-Symbol oben links im Wiedergabebildschirm, um die Untertiteleinstellungen vorzunehmen. Versuchen Sie, Tickets ab Montauk im Voraus zu kaufen, um die optimale Lösung zu finden – nach Preis, Transfers und anderen Parametern. Wohnungen Trogir WOHNUNGEN 1 und 4: A4 + 2 (zweiter Stock) „Applications.js mangler.“ Farbe: ZA68E. Länge: 45 cm. Die Mitte des SMI-Sicherheitsmerkmals „Mint Mark SI“ ist mit bloßem Auge nicht sichtbar, obwohl das Sicherheitsmerkmal beim Betrachten durch die einzigartige Dekodierungslinse sichtbar wird. Wir helfen Ihnen bei allen Fragen, versorgen Sie mit Ersatzteilen und beraten Sie, wie Sie Ihre Anlage energieeffizienter, wirtschaftlicher und sicherer machen. (3) Unsere Allgemeinen Geschäftsbedingungen gelten sowohl gegenüber Verbrauchern als auch gegenüber Unternehmern, sofern in der jeweiligen Klausel keine abweichende Regelung getroffen wird. So lässt sich mit wenigen Worten die unberechenbare Stadt Berlin beschreiben. Top-Vertreter in Dänemark für die E-Global Trade & Finance Group. Wir hatten ein ausgezeichnetes Abendessen und planten dann den nächsten Tag. Das Dom Wakacyjny ODSAPKA bietet Unterkünfte in Zieleniewo. Kostenlose Privatparkplätze stehen vor Ort zur Verfügung. Ein wunderbarer Begleiter für Ihr Zuhause, Ihren Urlaub oder Ihr Spa. Ich konnte nicht aus dem Bett aufstehen, konnte mich nicht alleine anziehen und ich brauchte die Hilfe anderer, die all diese Dinge für mich erledigten. § 5 Gewährleistung und Schadensersatz Lage Wenn Sie im Das Sonnbichl - Genusshotel - Adults only in Sankt Anton am Arlberg übernachten, sind Sie in der Nähe von Skipisten und ... Mit HSM Dokumente digital signieren oder beglaubigen Suchen Der Ruf Jesu treibt jeden voran Es ist uns wichtig, niemals an der Oberfläche der Dinge stehen zu bleiben, insbesondere wenn wir es mit einer Person zu tun haben. Hochschule für Musik Köln, Abteilung Wuppertal Es ist kein Zufall, dass die Komintern/ML hier mit gutem Beispiel vorangeht, Flagge hisst und das Feuer eröffnet. Dafür brauchen wir einen Karosseriebauer. Villa / Einfamilienhaus Lisboa Begriffsdefinition, Kennzeichnung und Installationsvorschriften In den Warenkorb legen Nachricht 34 Großhandel – Hochwertige königsblaue Anzüge für Männer Slim Fit Bräutigam Smoking Anzugjacke Maßgeschneiderter Hochzeitsanzug mit zwei Knöpfen (Jacke + Hose + Weste) Dies ist ein Ort, an dem Sie können sich beraten lassen, Ihre Erfahrungen diskutieren und Informationen mit anderen Kunden und Fans austauschen, um noch mehr aus Ihren Sony-Produkten und -Services herauszuholen. Maschinenersatzteile? Komplette Baugruppen? Prototypen oder Sonderanfertigungen für die Forschung: Fragen Sie uns gerne. Hotels Princes Risborough Die Kombination von Schnorcheln und Sporttauchen mit Meeresbiologie-Ausbildung gibt Schülern, Lehrern und Wissenschaftlern die Möglichkeit, das Meer von innen zu beobachten und die komplexen Beziehungen zwischen seinen Bewohnern direkt mitzuerleben. Kleiner Raum, aber sauber und komfortabel. Charm-Halskette „Skorpion / Nov“ – SET0207 – Charm Club – THOMAS SABO - Luxembourg Die wässrige Harnstofflösung reduziert den Stickoxidausstoß von Dieselmotoren deutlich und sorgt so für eine außergewöhnlich saubere Lösung. Ich spreche von seriösen Statistiken. Wie kommt es, dass ich, wenn ich sexuellen Missbrauch von Kindern live sehen wollte, mit virtueller Kinderpornografie in Kontakt treten kann? Sie machen es. Aufwärts durch herrliche Bergwälder zur „Croda da Lago“ und dem Rifugio. Natürlich & ursprünglich: Rustico Fries"""

# calculate the scores
scores = rouge_calculator.get_scores(text_to_be_evaluated, reference_text)

# print the scores
for score_dict in scores:
    for key, value in score_dict.items():
        print(key)
        for key2, value2 in value.items():
            print("\t", key2, ":", value2)

