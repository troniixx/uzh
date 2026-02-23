import sys
from readability_analysis import TextMetricsAnalyzer, FleschKincaidGradeLevel, GunningFogIndex

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        with open(filename) as f:
            text = [line.strip() for line in f]
        analyzer = TextMetricsAnalyzer()
        fk_index = FleschKincaidGradeLevel()
        gf_index = GunningFogIndex()

        text_metrics = analyzer.calculate_text_metrics(text)
        fk_value, fk_interpretation = fk_index.calculate_and_interpret(text_metrics)
        gf_value, gf_interpretation = gf_index.calculate_and_interpret(text_metrics)

        print(f"Flesch-Kincaid Grade Level Index: {fk_value}")
        print(f"Flesch-Kincaid Grade Level Interpretation: {fk_interpretation}")
        print()
        print(f"Gunning Fog Index: {gf_value}")
        print(f"Gunning Fog Index Interpretation: {gf_interpretation}")

    except IndexError:
        print("Please provide the filename as a command-line argument.")
    except FileNotFoundError:
        print("The specified file was not found.")