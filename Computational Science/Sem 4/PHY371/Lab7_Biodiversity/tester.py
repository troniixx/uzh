import pandas as pd
import numpy as np

class Tester:
    def __init__(self, path):
        self.labels = pd.read_csv(path).to_numpy()[:,4:]

    def test(self, preds):
        """
        preds: numpy array consisting of 0s (absent) and 1s (present). Shape: 10013 locations x 30 species
        """

        assert preds.shape == self.labels.shape
        assert np.count_nonzero((preds!=0) & (preds!=1))==0

        acc = (preds == self.labels).sum()/(preds.shape[0] * preds.shape[1])

        tp = preds * self.labels        # where preds = 1 and labels = 1
        tp = tp.sum()
        fp = preds * (1 - self.labels)  # where preds = 1 and labels = 0
        fp = fp.sum()
        fn = (1 - preds) * self.labels  # where preds = 0 and labels = 1
        fn = fn.sum()
        f1 = 2 * tp / (2 * tp + fp + fn)
        
        print("Accuracy: %.4f"%acc)
        print("F1-score: %.4f"%f1)
        print("Mean predicted per location: %.2f"%(preds.sum()/len(preds)))


if __name__ == "__main__":
    sf = Tester("./data/test_pa/SWItest_pa.csv")
    sf.test(np.ones((10013, 30)))
    # Model achieved an accuracy of 0.0809 
    # Model achieved a F1-score of 0.1497
    sf.test(np.zeros((10013, 30)))
    # Model achieved an accuracy of 0.9191
    # Model achieved a F1-score of 0.0000