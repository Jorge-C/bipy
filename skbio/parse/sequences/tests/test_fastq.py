#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Copyright (c) 2013--, scikit-bio development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import division

from skbio.parse.sequences import parse_fastq
from skbio.core.exception import FastqParseError
from unittest import TestCase, main


class ParseFastqTests(TestCase):

    def setUp(self):
        """ Initialize variables to be used by the tests """
        self.FASTQ_EXAMPLE = FASTQ_EXAMPLE.split('\n')
        self.FASTQ_EXAMPLE_2 = FASTQ_EXAMPLE_2.split('\n')

    def test_parse(self):
        """sequence and info objects should correctly match"""
        for label, seq, qual in parse_fastq(self.FASTQ_EXAMPLE):
            self.assertTrue(label in DATA)
            self.assertEqual(seq, DATA[label]["seq"])
            self.assertEqual(qual, DATA[label]["qual"])

    def test_parse_error(self):
        """Does this raise a FastqParseError with incorrect input?"""
        with self.assertRaises(FastqParseError):
            list(parse_fastq(self.FASTQ_EXAMPLE_2, strict=True))

DATA = {
    "GAPC_0015:6:1:1259:10413#0/1":
    dict(seq='AACACCAAACTTCTCCACCACGTGAGCTACAAAAG',
         qual=r'````Y^T]`]c^cabcacc`^Lb^ccYT\T\Y\WF'),
    "GAPC_0015:6:1:1283:11957#0/1":
    dict(seq='TATGTATATATAACATATACATATATACATACATA',
         qual=r']KZ[PY]_[YY^```ac^\\`bT``c`\aT``bbb'),
    "GAPC_0015:6:1:1284:10484#0/1":
    dict(seq='TCAGTTTTCCTCGCCATATTTCACGTCCTAAAGCG',
         qual=r'UM_]]U_]Z_Y^\^^``Y]`^SZ]\Ybb`^_LbL_'),
    "GAPC_0015:6:1:1287:17135#0/1":
    dict(seq='TGTGCCTATGGAAGCAGTTCTAGGATCCCCTAGAA',
         qual=r'^aacccL\ccc\c\cTKTS]KZ\]]I\[Wa^T`^K'),
    "GAPC_0015:6:1:1293:3171#0/1":
    dict(seq="AAAGAAAGGAAGAAAAGAAAAAGAAACCCGAGTTA",
             qual=r"b`bbbU_[YYcadcda_LbaaabWbaacYcc`a^c"),
    "GAPC_0015:6:1:1297:10729#0/1":
    dict(seq="TAATGCCAAAGAAATATTTCCAAACTACATGCTTA",
             qual=r"T\ccLbb``bacc]_cacccccLccc\ccTccYL^"),
    "GAPC_0015:6:1:1299:5940#0/1":
    dict(seq="AATCAAGAAATGAAGATTTATGTATGTGAAGAATA",
             qual=r"dcddbcfffdfffd`dd`^`c`Oc`Ybb`^eecde"),
    "GAPC_0015:6:1:1308:6996#0/1":
    dict(seq="TGGGACACATGTCCATGCTGTGGTTTTAACCGGCA",
             qual=r"a]`aLY`Y^^ccYa`^^TccK_X]\c\c`caTTTc"),
    "GAPC_0015:6:1:1314:13295#0/1":
    dict(seq="AATATTGCTTTGTCTGAACGATAGTGCTCTTTGAT",
         qual=r"cLcc\\dddddaaYd`T```bLYT\`a```bZccc"),
    "GAPC_0015:6:1:1317:3403#0/1":
    dict(seq="TTGTTTCCACTTGGTTGATTTCACCCCTGAGTTTG",
         # had to add space in qual line
         qual=r"\\\ZTYTSaLbb``\_UZ_bbcc`cc^[ac\a\Tc ".strip())
}

FASTQ_EXAMPLE = r"""@GAPC_0015:6:1:1259:10413#0/1
AACACCAAACTTCTCCACCACGTGAGCTACAAAAG
+GAPC_0015:6:1:1259:10413#0/1
````Y^T]`]c^cabcacc`^Lb^ccYT\T\Y\WF
@GAPC_0015:6:1:1283:11957#0/1
TATGTATATATAACATATACATATATACATACATA
+GAPC_0015:6:1:1283:11957#0/1
]KZ[PY]_[YY^```ac^\\`bT``c`\aT``bbb
@GAPC_0015:6:1:1284:10484#0/1
TCAGTTTTCCTCGCCATATTTCACGTCCTAAAGCG
+GAPC_0015:6:1:1284:10484#0/1
UM_]]U_]Z_Y^\^^``Y]`^SZ]\Ybb`^_LbL_
@GAPC_0015:6:1:1287:17135#0/1
TGTGCCTATGGAAGCAGTTCTAGGATCCCCTAGAA
+GAPC_0015:6:1:1287:17135#0/1
^aacccL\ccc\c\cTKTS]KZ\]]I\[Wa^T`^K
@GAPC_0015:6:1:1293:3171#0/1
AAAGAAAGGAAGAAAAGAAAAAGAAACCCGAGTTA
+GAPC_0015:6:1:1293:3171#0/1
b`bbbU_[YYcadcda_LbaaabWbaacYcc`a^c
@GAPC_0015:6:1:1297:10729#0/1
TAATGCCAAAGAAATATTTCCAAACTACATGCTTA
+GAPC_0015:6:1:1297:10729#0/1
T\ccLbb``bacc]_cacccccLccc\ccTccYL^
@GAPC_0015:6:1:1299:5940#0/1
AATCAAGAAATGAAGATTTATGTATGTGAAGAATA
+GAPC_0015:6:1:1299:5940#0/1
dcddbcfffdfffd`dd`^`c`Oc`Ybb`^eecde
@GAPC_0015:6:1:1308:6996#0/1
TGGGACACATGTCCATGCTGTGGTTTTAACCGGCA
+GAPC_0015:6:1:1308:6996#0/1
a]`aLY`Y^^ccYa`^^TccK_X]\c\c`caTTTc
@GAPC_0015:6:1:1314:13295#0/1
AATATTGCTTTGTCTGAACGATAGTGCTCTTTGAT
+GAPC_0015:6:1:1314:13295#0/1
cLcc\\dddddaaYd`T```bLYT\`a```bZccc
@GAPC_0015:6:1:1317:3403#0/1
TTGTTTCCACTTGGTTGATTTCACCCCTGAGTTTG
+GAPC_0015:6:1:1317:3403#0/1
\\\ZTYTSaLbb``\_UZ_bbcc`cc^[ac\a\Tc"""

FASTQ_EXAMPLE_2 = r"""@GAPC_0017:6:1:1259:10413#0/1
AACACCAAACTTCTCCACCACGTGAGCTACAAAAG
+GAPC_0015:6:1:1259:10413#0/1
````Y^T]`]c^cabcacc`^Lb^ccYT\T\Y\WF
@GAPC_0015:6:1:1283:11957#0/1
TATGTATATATAACATATACATATATACATACATA
+GAPC_0015:6:1:1283:11957#0/1
]KZ[PY]_[YY^```ac^\\`bT``c`\aT``bbb
@GAPC_0015:6:1:1284:10484#0/1
"""

if __name__ == "__main__":
    main()
