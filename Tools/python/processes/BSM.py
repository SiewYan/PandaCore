#!/usr/bin/env python
'''@package docstring
Just a giant list of processes and properties
'''

processes =    {
    'TTbarDMJets_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('TTbarDM','MC',1),

    'thq':('thq','MC',0.7927),
    'thw':('thw','MC',0.147),

    'GluGlu_HToInvisible_M125_13TeV_powheg_pythia8':('ggFHinv','MC',48.6),
    'VBF_HToInvisible_M125_13TeV_powheg_pythia8':('vbfHinv_m125','MC',3.78),
    # below are normalized to m125 - only want to see acceptance effects as a function of mH
    'VBF_HToInvisible_M110_13TeV_powheg_pythia8':('vbfHinv_m110','MC',3.78),
    'VBF_HToInvisible_M150_13TeV_powheg_pythia8':('vbfHinv_m150','MC',3.78),
    'VBF_HToInvisible_M200_13TeV_powheg_pythia8':('vbfHinv_m200','MC',3.78),
    'VBF_HToInvisible_M300_13TeV_powheg_pythia8':('vbfHinv_m300','MC',3.78),
    'VBF_HToInvisible_M500_13TeV_powheg_pythia8':('vbfHinv_m500','MC',3.78),
    'VBF_HToInvisible_M600_13TeV_powheg_pythia8':('vbfHinv_m600','MC',3.78),
    'VBF_HToInvisible_M800_13TeV_powheg_pythia8':('vbfHinv_m800','MC',3.78),
    'VBF_HToInvisible_M1000_13TeV_powheg_pythia8':('vbfHinv_m1000','MC',3.78),

    'ZprimeToTTJet_M-500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-500','MC',1),
    'ZprimeToTTJet_M-750_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-750','MC',1),
    'ZprimeToTTJet_M-1000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1000','MC',1),
    'ZprimeToTTJet_M-1250_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1250','MC',1),
    'ZprimeToTTJet_M-1500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1500','MC',1),
    'ZprimeToTTJet_M-2000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-2000','MC',1),
    'ZprimeToTTJet_M-2500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-2500','MC',1),
    'ZprimeToTTJet_M-3000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-3000','MC',1),
    'ZprimeToTTJet_M-3500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-3500','MC',1),
    'ZprimeToTTJet_M-4000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-4000','MC',1),

    'thq':('thq','MC',0.7927),
    'thw':('thw','MC',0.147),

    'ZprimeToWW_narrow_M-800_13TeV-madgraph':('ZpWW_med-800','MC',1),
    'ZprimeToWW_narrow_M-1000_13TeV-madgraph':('ZpWW_med-1000','MC',1),
    'ZprimeToWW_narrow_M-1200_13TeV-madgraph':('ZpWW_med-1200','MC',1),
    'ZprimeToWW_narrow_M-1400_13TeV-madgraph':('ZpWW_med-1400','MC',1),
    'ZprimeToWW_narrow_M-1600_13TeV-madgraph':('ZpWW_med-1600','MC',1),
    'ZprimeToWW_narrow_M-1800_13TeV-madgraph':('ZpWW_med-1800','MC',1),
    'ZprimeToWW_narrow_M-2000_13TeV-madgraph':('ZpWW_med-2000','MC',1),
    'ZprimeToWW_narrow_M-2500_13TeV-madgraph':('ZpWW_med-2500','MC',1),

    'ST_tch_DM-scalar_LO-100_1-13_TeV':('ST_tch_DM-scalar_LO-100_1-13_TeV','MC',0.293*0.68),
    'ST_tch_DM-scalar_LO-300_1-13_TeV':('ST_tch_DM-scalar_LO-300_1-13_TeV','MC',0.03202*0.68),
    'ST_tch_DM-scalar_LO-500_1-13_TeV':('ST_tch_DM-scalar_LO-500_1-13_TeV','MC',0.004996*0.68),
    'ST_tch_DM-scalar_LO-1000_1-13_TeV':('ST_tch_DM-scalar_LO-1000_1-13_TeV','MC',0.0003009*0.68),

    'TT_DM-scalar_LO-300_1-13_TeV':('TT_DM-scalar_LO-300_1-13_TeV','MC',0.03045),
    'TT_DM-scalar_LO-500_1-13_TeV':('TT_DM-scalar_LO-500_1-13_TeV','MC',0.004947),
    'TT_DM-scalar_LO-1000_1-13_TeV':('TT_DM-scalar_LO-1000_1-13_TeV','MC',0.000736),

    'MonoHbb_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10_dm-1','MC',1.4971719048020),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10_dm-10','MC',0.0068827725015),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10_dm-50','MC',0.0001182107976),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10_dm-150','MC',0.0000102513973),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10_dm-500','MC',0.0000000026006),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10_dm-1000','MC',0.0000000000160),
    'MonoHbb_ZpBaryonic_MZp-15_MChi-10_13TeV-madgraph':('ZpBaryonic_med-15_dm-10','MC',0.0241243264082),
    'MonoHbb_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph':('ZpBaryonic_med-20_dm-1','MC',1.5708303614837),
    'MonoHbb_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph':('ZpBaryonic_med-50_dm-1','MC',1.8787525219888),
    'MonoHbb_ZpBaryonic_MZp-50_MChi-10_13TeV-madgraph':('ZpBaryonic_med-50_dm-10','MC',1.8686472610676),
    'MonoHbb_ZpBaryonic_MZp-50_MChi-50_13TeV-madgraph':('ZpBaryonic_med-50_dm-50','MC',0.0041445173799),
    'MonoHbb_ZpBaryonic_MZp-95_MChi-50_13TeV-madgraph':('ZpBaryonic_med-95_dm-50','MC',0.1070881411920),
    'MonoHbb_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph':('ZpBaryonic_med-100_dm-1','MC',1.8350014490170),
    'MonoHbb_ZpBaryonic_MZp-100_MChi-10_13TeV-madgraph':('ZpBaryonic_med-100_dm-10','MC',1.8311374853540),
    'MonoHbb_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph':('ZpBaryonic_med-200_dm-1','MC',1.4723542212437),
    'MonoHbb_ZpBaryonic_MZp-200_MChi-50_13TeV-madgraph':('ZpBaryonic_med-200_dm-50','MC',1.2073355514877),
    'MonoHbb_ZpBaryonic_MZp-200_MChi-150_13TeV-madgraph':('ZpBaryonic_med-200_dm-150','MC',0.0018402642784),
    'MonoHbb_ZpBaryonic_MZp-295_MChi-150_13TeV-madgraph':('ZpBaryonic_med-295_dm-150','MC',0.0772562835636),
    'MonoHbb_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph':('ZpBaryonic_med-300_dm-1','MC',1.3081597528204),
    'MonoHbb_ZpBaryonic_MZp-300_MChi-50_13TeV-madgraph':('ZpBaryonic_med-300_dm-50','MC',1.1234969709678),
    'MonoHbb_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph':('ZpBaryonic_med-500_dm-1','MC',0.6310480800692),
    'MonoHbb_ZpBaryonic_MZp-500_MChi-150_13TeV-madgraph':('ZpBaryonic_med-500_dm-150','MC',0.3922022706199),
    'MonoHbb_ZpBaryonic_MZp-500_MChi-500_13TeV-madgraph':('ZpBaryonic_med-500_dm-500','MC',0.0000118690907),
    'MonoHbb_ZpBaryonic_MZp-995_MChi-500_13TeV-madgraph':('ZpBaryonic_med-995_dm-500','MC',0.0000000466117),
    'MonoHbb_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1','MC',0.1164211478301),
    'MonoHbb_ZpBaryonic_MZp-1000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-1000_dm-150','MC',0.1130981455808),
    'MonoHbb_ZpBaryonic_MZp-1000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1000','MC',0.0000003182419),
    'MonoHbb_ZpBaryonic_MZp-1995_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1995_dm-1000','MC',0.0004210309298),
    'MonoHbb_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-2000_dm-1','MC',0.0080403926209),
    'MonoHbb_ZpBaryonic_MZp-2000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-2000_dm-500','MC',0.0073116588302),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1','MC',0.0000000068756),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10000_dm-10','MC',0.0000000068844),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10000_dm-50','MC',0.0000000068310),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10000_dm-150','MC',0.0000000066844),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10000_dm-500','MC',0.0000000055185),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1000','MC',0.0000000038070),

    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph':('ZpA0h_med-800_dm-600','MC',0.010101*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph':('ZpA0h_med-800_dm-500','MC',0.0367*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph':('ZpA0h_med-800_dm-400','MC',0.091124*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph':('ZpA0h_med-800_dm-300','MC',0.27765*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph':('ZpA0h_med-600_dm-400','MC',0.063916*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph':('ZpA0h_med-600_dm-300','MC',0.45127*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph':('ZpA0h_med-2500_dm-800','MC',0.0007806*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph':('ZpA0h_med-2500_dm-700','MC',0.0008699*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph':('ZpA0h_med-2500_dm-600','MC',0.0009678*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph':('ZpA0h_med-2500_dm-500','MC',0.0010859*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph':('ZpA0h_med-2500_dm-400','MC',0.0013246*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph':('ZpA0h_med-2500_dm-300','MC',0.0025458*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph':('ZpA0h_med-2000_dm-800','MC',0.0020981*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph':('ZpA0h_med-2000_dm-700','MC',0.0024651*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-600_13TeV-madgraph':('ZpA0h_med-2000_dm-600','MC',0.0028691*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph':('ZpA0h_med-2000_dm-500','MC',0.003341*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph':('ZpA0h_med-2000_dm-400','MC',0.0041934*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph':('ZpA0h_med-2000_dm-300','MC',0.0082317*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph':('ZpA0h_med-1700_dm-800','MC',0.0036537*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph':('ZpA0h_med-1700_dm-700','MC',0.0045823*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph':('ZpA0h_med-1700_dm-600','MC',0.0056149*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph':('ZpA0h_med-1700_dm-500','MC',0.0068221*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-400_13TeV-madgraph':('ZpA0h_med-1700_dm-400','MC',0.0088466*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph':('ZpA0h_med-1700_dm-300','MC',0.017786*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph':('ZpA0h_med-1400_dm-800','MC',0.0055221*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph':('ZpA0h_med-1400_dm-700','MC',0.0079659*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph':('ZpA0h_med-1400_dm-600','MC',0.010822*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph':('ZpA0h_med-1400_dm-500','MC',0.014225*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph':('ZpA0h_med-1400_dm-400','MC',0.019609*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph':('ZpA0h_med-1400_dm-300','MC',0.041208*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph':('ZpA0h_med-1200_dm-800','MC',0.005655*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph':('ZpA0h_med-1200_dm-700','MC',0.010028*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph':('ZpA0h_med-1200_dm-600','MC',0.015763*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph':('ZpA0h_med-1200_dm-500','MC',0.022935*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph':('ZpA0h_med-1200_dm-400','MC',0.034039*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph':('ZpA0h_med-1200_dm-300','MC',0.075451*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph':('ZpA0h_med-1000_dm-800','MC',0.0027483*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph':('ZpA0h_med-1000_dm-700','MC',0.0085776*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph':('ZpA0h_med-1000_dm-600','MC',0.01897*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph':('ZpA0h_med-1000_dm-500','MC',0.03431*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph':('ZpA0h_med-1000_dm-400','MC',0.058824*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph':('ZpA0h_med-1000_dm-300','MC',0.14383*0.578),

    'MonoHbb_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10_dm-1','MC',2.594752001*0.578),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10_dm-10','MC',0.0119285485*0.578),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10_dm-50','MC',0.00020487139962*0.578),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10_dm-150','MC',3.14857697501e-06*0.578),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10_dm-500','MC',4.5071850285e-09*0.578),
    'MonoHbb_ZpBaryonic_MZp-10_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10_dm-1000','MC',2.7728742863e-11*0.578),
    'MonoHbb_ZpBaryonic_MZp-15_MChi-10_13TeV-madgraph':('ZpBaryonic_med-15_dm-10','MC',0.041809924451*0.578),
    'MonoHbb_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph':('ZpBaryonic_med-20_dm-1','MC',2.72240963862*0.578),
    'MonoHbb_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph':('ZpBaryonic_med-50_dm-1','MC',3.25607022875*0.578),
    'MonoHbb_ZpBaryonic_MZp-50_MChi-10_13TeV-madgraph':('ZpBaryonic_med-50_dm-10','MC',3.23855677828*0.578),
    'MonoHbb_ZpBaryonic_MZp-50_MChi-50_13TeV-madgraph':('ZpBaryonic_med-50_dm-50','MC',0.00718287240877*0.578),
    'MonoHbb_ZpBaryonic_MZp-95_MChi-50_13TeV-madgraph':('ZpBaryonic_med-95_dm-50','MC',0.185594698773*0.578),
    'MonoHbb_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph':('ZpBaryonic_med-100_dm-1','MC',3.18024514561*0.578),
    'MonoHbb_ZpBaryonic_MZp-100_MChi-10_13TeV-madgraph':('ZpBaryonic_med-100_dm-10','MC',3.17354850148*0.578),
    'MonoHbb_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph':('ZpBaryonic_med-200_dm-1','MC',2.5517404181*0.578),
    'MonoHbb_ZpBaryonic_MZp-200_MChi-50_13TeV-madgraph':('ZpBaryonic_med-200_dm-50','MC',2.09243596445*0.578),
    'MonoHbb_ZpBaryonic_MZp-200_MChi-150_13TeV-madgraph':('ZpBaryonic_med-200_dm-150','MC',0.00318936616712*0.578),
    'MonoHbb_ZpBaryonic_MZp-295_MChi-150_13TeV-madgraph':('ZpBaryonic_med-295_dm-150','MC',0.133893039105*0.578),
    'MonoHbb_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph':('ZpBaryonic_med-300_dm-1','MC',2.26717461494*0.578),
    'MonoHbb_ZpBaryonic_MZp-300_MChi-50_13TeV-madgraph':('ZpBaryonic_med-300_dm-50','MC',1.94713513166*0.578),
    'MonoHbb_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph':('ZpBaryonic_med-500_dm-1','MC',1.09367084934*0.578),
    'MonoHbb_ZpBaryonic_MZp-500_MChi-150_13TeV-madgraph':('ZpBaryonic_med-500_dm-150','MC',0.679726638856*0.578),
    'MonoHbb_ZpBaryonic_MZp-500_MChi-500_13TeV-madgraph':('ZpBaryonic_med-500_dm-500','MC',2.05703477766e-05*0.578),
    'MonoHbb_ZpBaryonic_MZp-995_MChi-500_13TeV-madgraph':('ZpBaryonic_med-995_dm-500','MC',0.0111215826866*0.578),
    'MonoHbb_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1','MC',0.201769753605*0.578),
    'MonoHbb_ZpBaryonic_MZp-1000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-1000_dm-150','MC',0.19601065092*0.578),
    'MonoHbb_ZpBaryonic_MZp-1000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1000','MC',5.51545710471e-07*0.578),
    'MonoHbb_ZpBaryonic_MZp-1995_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1995_dm-1000','MC',0.000729689653045*0.578),
    'MonoHbb_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-2000_dm-1','MC',0.0139348225665*0.578),
    'MonoHbb_ZpBaryonic_MZp-2000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-2000_dm-500','MC',0.012671852392*0.578),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1','MC',1.19161364309e-08*0.578),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10000_dm-10','MC',1.19314052769e-08*0.578),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10000_dm-50','MC',1.18388857948e-08*0.578),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10000_dm-150','MC',1.15848042141e-08*0.578),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10000_dm-500','MC',9.56417074962e-09*0.578),
    'MonoHbb_ZpBaryonic_MZp-10000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1000','MC',6.59793071766e-09*0.578),

    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2750_MA0-300_13TeV-madgraph':('ZpA0h_med-2750_dm-300','MC',0.0015511*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2750_MA0-500_13TeV-madgraph':('ZpA0h_med-2750_dm-500','MC',0.00067388*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2750_MA0-800_13TeV-madgraph':('ZpA0h_med-2750_dm-800','MC',0.00050351*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-3000_MA0-300_13TeV-madgraph':('ZpA0h_med-3000_dm-300','MC',0.00092077*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-3000_MA0-500_13TeV-madgraph':('ZpA0h_med-3000_dm-500','MC',0.0004022*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-3000_MA0-800_13TeV-madgraph':('ZpA0h_med-3000_dm-800','MC',0.00030894*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-3500_MA0-300_13TeV-madgraph':('ZpA0h_med-3500_dm-300','MC',0.00033718*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-3500_MA0-500_13TeV-madgraph':('ZpA0h_med-3500_dm-500','MC',0.00014885*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-3500_MA0-800_13TeV-madgraph':('ZpA0h_med-3500_dm-800','MC',0.00011855*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-4000_MA0-300_13TeV-madgraph':('ZpA0h_med-4000_dm-300','MC',0.00012964*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-4000_MA0-500_13TeV-madgraph':('ZpA0h_med-4000_dm-500','MC',5.7149e-05*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-4000_MA0-800_13TeV-madgraph':('ZpA0h_med-4000_dm-800','MC',4.6312e-05*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph':('ZpA0h_med-800_dm-600','MC',0.010350*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph':('ZpA0h_med-800_dm-500','MC',0.037616*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph':('ZpA0h_med-800_dm-400','MC',0.093376*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph':('ZpA0h_med-800_dm-300','MC',0.2848*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph':('ZpA0h_med-600_dm-400','MC',0.065307*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph':('ZpA0h_med-600_dm-300','MC',0.46223*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph':('ZpA0h_med-2500_dm-800','MC',0.00082449*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph':('ZpA0h_med-2500_dm-700','MC',0.00091718*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph':('ZpA0h_med-2500_dm-600','MC',0.0010187*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph':('ZpA0h_med-2500_dm-500','MC',0.0011446*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph':('ZpA0h_med-2500_dm-400','MC',0.0013922*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph':('ZpA0h_med-2500_dm-300','MC',0.0026787*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph':('ZpA0h_med-2000_dm-800','MC',0.0021931*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph':('ZpA0h_med-2000_dm-700','MC',0.0025816*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-600_13TeV-madgraph':('ZpA0h_med-2000_dm-600','MC',0.0029991*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph':('ZpA0h_med-2000_dm-500','MC',0.0034998*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph':('ZpA0h_med-2000_dm-400','MC',0.0043899*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph':('ZpA0h_med-2000_dm-300','MC',0.0086008*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph':('ZpA0h_med-1700_dm-800','MC',0.0038043*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph':('ZpA0h_med-1700_dm-700','MC',0.0047758*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph':('ZpA0h_med-1700_dm-600','MC',0.0058468*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph':('ZpA0h_med-1700_dm-500','MC',0.0071071*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-400_13TeV-madgraph':('ZpA0h_med-1700_dm-400','MC',0.0092082*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph':('ZpA0h_med-1700_dm-300','MC',0.018545*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph':('ZpA0h_med-1400_dm-800','MC',0.0057179*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph':('ZpA0h_med-1400_dm-700','MC',0.0082681*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph':('ZpA0h_med-1400_dm-600','MC',0.011224*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph':('ZpA0h_med-1400_dm-500','MC',0.014723*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph':('ZpA0h_med-1400_dm-400','MC',0.020306*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph':('ZpA0h_med-1400_dm-300','MC',0.042687*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph':('ZpA0h_med-1200_dm-800','MC',0.0058353*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph':('ZpA0h_med-1200_dm-700','MC',0.010364*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph':('ZpA0h_med-1200_dm-600','MC',0.016254*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph':('ZpA0h_med-1200_dm-500','MC',0.023706*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph':('ZpA0h_med-1200_dm-400','MC',0.03524*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph':('ZpA0h_med-1200_dm-300','MC',0.078164*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph':('ZpA0h_med-1000_dm-800','MC',0.00283922*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph':('ZpA0h_med-1000_dm-700','MC',0.00881814*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph':('ZpA0h_med-1000_dm-600','MC',0.019542*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph':('ZpA0h_med-1000_dm-500','MC',0.035347*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph':('ZpA0h_med-1000_dm-400','MC',0.060531*0.578),
    'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph':('ZpA0h_med-1000_dm-300','MC',0.14771*0.578),

    'TTbarDMJets_scalar_Mchi-10_Mphi-100' : ('TTbarDMJets_scalar_Mchi-10_Mphi-100','MC',1),
    'TTbarDMJets_scalar_Mchi-10_Mphi-10' : ('TTbarDMJets_scalar_Mchi-10_Mphi-10','MC',1),
    'TTbarDMJets_scalar_Mchi-10_Mphi-15' : ('TTbarDMJets_scalar_Mchi-10_Mphi-15','MC',1),
    'TTbarDMJets_scalar_Mchi-10_Mphi-50' : ('TTbarDMJets_scalar_Mchi-10_Mphi-50','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-10000' : ('TTbarDMJets_scalar_Mchi-1_Mphi-10000','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-100' : ('TTbarDMJets_scalar_Mchi-1_Mphi-100','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-10' : ('TTbarDMJets_scalar_Mchi-1_Mphi-10','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-200' : ('TTbarDMJets_scalar_Mchi-1_Mphi-200','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-20' : ('TTbarDMJets_scalar_Mchi-1_Mphi-20','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-300' : ('TTbarDMJets_scalar_Mchi-1_Mphi-300','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-500' : ('TTbarDMJets_scalar_Mchi-1_Mphi-500','MC',1),
    'TTbarDMJets_scalar_Mchi-1_Mphi-50' : ('TTbarDMJets_scalar_Mchi-1_Mphi-50','MC',1),
    'TTbarDMJets_scalar_Mchi-50_Mphi-10' : ('TTbarDMJets_scalar_Mchi-50_Mphi-10','MC',1),
    'TTbarDMJets_scalar_Mchi-50_Mphi-200' : ('TTbarDMJets_scalar_Mchi-50_Mphi-200','MC',1),
    'TTbarDMJets_scalar_Mchi-50_Mphi-300' : ('TTbarDMJets_scalar_Mchi-50_Mphi-300','MC',1),
    'TTbarDMJets_scalar_Mchi-50_Mphi-50' : ('TTbarDMJets_scalar_Mchi-50_Mphi-50','MC',1),
    'TTbarDMJets_scalar_Mchi-50_Mphi-95' : ('TTbarDMJets_scalar_Mchi-50_Mphi-95','MC',1),
}
