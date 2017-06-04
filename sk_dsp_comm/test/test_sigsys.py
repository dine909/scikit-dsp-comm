from unittest import TestCase

import numpy as np
from numpy.random import randn
import numpy.testing as npt
from sk_dsp_comm import sigsys as ss


class TestSigsys(TestCase):

    def test_cic_case_1(self):
        correct = np.ones(10) / 10
        b = ss.CIC(10,1)
        diff = correct - b
        diff = np.sum(diff)
        self.assertEqual(diff, 0)

    def test_cic_case_2(self):
        correct = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1,
                   0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]
        b = ss.CIC(10, 2)
        diff = correct - b
        diff = np.sum(diff)
        self.assertEqual(diff, 0)

    def test_ten_band_equalizer(self):
        w = randn(1000000)
        gdB = [x for x in range(1, 11)]
        y = ss.ten_band_eq_filt(w,gdB)
        yavg = np.average(y)
        npt.assert_almost_equal(abs(yavg), 0.001, decimal=2)
