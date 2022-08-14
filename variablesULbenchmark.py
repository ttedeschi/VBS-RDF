from array import array
import numpy as np

'''
class variable(object):
    def __init__(self, name, title, nbins, xmin, xmax=None):
        self._name=name
        self._title=title
        self._nbins=nbins
        self._xmin=xmin
        if xmax==None:
            self._xmax=xmin[nbins]
            self._iscustom = True
        else:
            self._xmax=xmax
            self._iscustom = False

    def __str__(self):
        return  '\"'+str(self._name)+'\",\"'+str(self._title)+'\",\"'+str(self._taglio)+'\",'+str(self._nbins)+','+str(self._xmin)+','+str(self._xmax)
'''

class variable(object):
    def __init__(self, name, title, nbins, bins):
        self._name=name
        self._title=title
        self._nbins=nbins
        self._bins=bins
        self._iscustom = True
        self._xmin=bins
        self._xmax=bins[nbins]

        
        
           
        
variables = {}


bin_invm = {}
bin_invm['SR'] = array("d", [600., 800., 1000., 1200., 1400., 1600., 1800., 2000., 2400.])
bin_invm['fakes_CR'] = array("d", [0., 400., 600., 800., 1000., 1200., 1440., 1600., 2000., 2400.])
bin_invm['OS_CR_bvetoL'] = bin_invm['fakes_CR']
bin_invm['ttbar_CR'] = array("d", [0., 200., 400., 600., 800., 1000., 1200., 1440., 1600., 2000., 2400., 2800.])
            
bin_m1T = array("d", [0., 100., 150., 200., 300., 500.])#, 1000.])
bin_mo1 = array("d", [0., 100., 150., 200., 300., 500.])#, 1000.])

bin_df = {}
bin_df["ttbar_CR"] = array("d", [0., 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0])   
bin_df["OS_CR_bvetoL"] = array("d", [0., 0.05, 0.1, 0.15, 0.2])  
bin_df['SR'] = array("d", [0., 0.1, 0.2, 0.4])   
bin_df['fakes_CR'] = array("d", [0., 0.1, 0.2, 0.4])   

bin_rt = {}
bin_rt['fakes_CR'] = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.4, 2.8, 3.2, 3.6, 4.4, 5.])
bin_rt['OS_CR_bvetoL'] = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.4, 2.8, 3.2, 3.6, 4.4, 5.])
bin_rt["ttbar_CR"] = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.8, 3.2, 3.6, 4.4, 5.])
bin_rt["SR"] = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.4, 1.8, 2.4, 5.])

bin_metpt = {}
bin_metpt["SR"] = array("d", [50., 100., 150., 200., 300.])
bin_metpt["OS_CR_bvetoL"] = array("d", [0., 10., 15., 20., 25., 30., 35., 40., 45., 50.])
bin_metpt["fakes_CR"] = array("d", [0., 10., 15., 20., 25., 30., 35., 40., 45., 50.])
bin_metpt["ttbar_CR"] = array("d", [50., 75., 100., 125., 150., 175., 200., 250., 300.])

bin_zepp = array("d", [-1., -0.7, -0.4, -0.2, 0., 0.2, 0.4, 0.7, 1.])
   
bin_ptRel = array("d", [0., 50., 75., 100., 125, 150., 175., 200., 225., 250.])
bin_ptRel_2 = array("d", [0., 50., 75., 100., 125, 150., 175., 200., 225., 250.])
        
bin_deltaeta_jj = array("d", [-8., -5., -3.5, -2.5, 2.5, 3.5, 5., 8.])
                                             
bin_taujetrelpt = array("d", [0.85, 0.9, 0.92, 0.94, 0.96, 0.98, 1.])

bin_mTs = {}
bin_mTs["SR"] = array("d", [0., 25., 50., 75., 100., 150., 200.])
bin_mTs["fakes_CR"] = array("d", [0., 25., 50., 75., 100., 125., 150.])
bin_mTs["OS_CR_bvetoL"] = array("d", [0., 25., 50., 75., 100., 125., 150., 200., 250.])
bin_mTs["ttbar_CR"] = array("d", [0., 25., 50., 75., 100., 125., 150., 200., 250.])

variables["SR"] = []
variables["SR"].append(variable('leadjet_pt',  'Lead jet p_{T} [GeV]', 9 ,array("f", [0., 50., 100., 150., 200., 250., 300., 400., 500., 600.])))
variables["SR"].append(variable('subleadjet_pt',  'Sublead jet p_{T} [GeV]', 5 , array("f", [0., 50., 100., 150., 250., 500.])))
variables["SR"].append(variable('lepton_pt',  'Lepton p_{T} [GeV]', 9 , array("f", [0., 30., 45., 60., 80., 100., 125., 150, 200., 250.]) ))
variables["SR"].append(variable('tau_pt',  'Tau p_{T} [GeV]', 8 , array("f", [30., 45., 60., 80., 100., 125., 150, 200., 250.])))
variables["SR"].append(variable('SMbdt', 'SM BDT output',  5, array("f", [0., 0.2, 0.4, 0.6, 0.8, 1.])))
variables["SR"].append(variable('m_jj', 'Invarant mass JJ',  4, array("f", [500., 700., 1000., 1500., 2500.])))
variables["SR"].append(variable('nJets', 'n jets', 11, array("f", list(np.linspace(-0.5, 10.5, 12)))))
variables["SR"].append(variable('nBJets', 'n bjets (DeepJet M)', 6, array("f", list(np.linspace(-0.5, 5.5, 7)))))
variables["SR"].append(variable('m_jjtau', 'invariant mass j_{1} j_{2} #tau [GeV]',  len(bin_invm["SR"]) - 1, bin_invm["SR"]))
variables["SR"].append(variable('m_jjtaulep', 'invariant mass j_{1} j_{2} #l #tau [GeV]',  len(bin_invm["SR"]) - 1, bin_invm["SR"]))
variables["SR"].append(variable('m_1T', 'M_{1T} [GeV]', len(bin_m1T) - 1, bin_m1T))
variables["SR"].append(variable('m_o1', 'M_{o1} [GeV]', len(bin_mo1) - 1 , bin_mo1))
variables["SR"].append(variable('tau_DeepTauVsEle_raw', '#tau DeepTauVsEle raw', 7, array("f", list(np.linspace(-0.3, 1, 8)))))
variables["SR"].append(variable('tau_DeepTauVsMu_raw', '#tau DeepTauVsMu raw', 7,array("f", list(np.linspace(-0.3, 1, 8)))))
variables["SR"].append(variable('leadjet_DeepFlv_b', 'leading jet DeepFlavour b raw',len(bin_df["SR"]) - 1, bin_df["SR"]))
variables["SR"].append(variable('subleadjet_DeepFlv_b', 'subleading jet DeepFlavour b raw', len(bin_df["SR"]) - 1, bin_df["SR"]))
variables["SR"].append(variable('lepton_pfRelIso04', 'lepton isolation', 15, array("f", list(np.linspace(0, 0.15, 16)))))
variables["SR"].append(variable('event_RT', 'R_{T}', len(bin_rt["SR"]) - 1, bin_rt["SR"]))
variables["SR"].append(variable('deltaPhi_jj', '#Delta #phi_{jj}', 14, array("f", list(np.linspace(-3.5, 3.5, 15)))))
variables["SR"].append(variable('MET_pt', 'p_{T}^{miss} [GeV]', len(bin_metpt["SR"]) - 1, bin_metpt["SR"]))
variables["SR"].append(variable('event_Zeppenfeld_over_deltaEta_jj', 'event Zeppenfeld',  len(bin_zepp) - 1, bin_zepp))
variables["SR"].append(variable('ptRel_tauj1', 'relative p_{T} #tau j_{1}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["SR"].append(variable('ptRel_tauj2', 'relative p_{T} #tau j_{2}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["SR"].append(variable('ptRel_lepj1', 'relative p_{T} #l j_{1}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["SR"].append(variable('ptRel_lepj2', 'relative p_{T} #l j_{2}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["SR"].append(variable('deltaEta_jj', '#Delta #eta_{jj}', len(bin_deltaeta_jj) - 1, bin_deltaeta_jj))
variables["SR"].append(variable('taujet_relpt',  '#tau jet relative p_{T}', len(bin_taujetrelpt) - 1, bin_taujetrelpt))
variables["SR"].append(variable('mT_lep_MET', 'M_{T}(#l, MET) [GeV]',  len(bin_mTs["SR"]) - 1, bin_mTs["SR"]))

    
variables["fakes_CR"] = []
variables["fakes_CR"].append(variable('leadjet_pt',  'Lead jet p_{T} [GeV]', 5 ,array("f", [0., 50., 100., 150., 250., 400.])))
variables["fakes_CR"].append(variable('subleadjet_pt',  'Sublead jet p_{T} [GeV]', 3 , array("f", [0., 50., 100., 200.])))
variables["fakes_CR"].append(variable('lepton_pt',  'Lepton p_{T} [GeV]', 7 , array("f", [0., 30., 45., 60., 80., 100., 150, 250.]) ))
variables["fakes_CR"].append(variable('tau_pt',  'Tau p_{T} [GeV]', 4 , array("f", [30., 45., 60., 100., 200.])))
variables["fakes_CR"].append(variable('SMbdt', 'SM BDT output',  5, array("f", [0., 0.2, 0.4, 0.6, 0.8, 1.])))
variables["fakes_CR"].append(variable('m_jj', 'Invarant mass JJ',  6, array("f", [0., 300., 500., 700., 1000., 1500., 2000.])))
variables["fakes_CR"].append(variable('nJets', 'n jets', 11, array("f", list(np.linspace(-0.5, 10.5, 12)))))
variables["fakes_CR"].append(variable('nBJets', 'n bjets (DeepJet M)', 6, array("f", list(np.linspace(-0.5, 5.5, 7)))))
variables["fakes_CR"].append(variable('m_jjtau', 'invariant mass j_{1} j_{2} #tau [GeV]',  len(bin_invm["fakes_CR"]) - 1, bin_invm["fakes_CR"]))
variables["fakes_CR"].append(variable('m_jjtaulep', 'invariant mass j_{1} j_{2} #l #tau [GeV]',  len(bin_invm["fakes_CR"]) - 1, bin_invm["fakes_CR"]))
variables["fakes_CR"].append(variable('m_1T', 'M_{1T} [GeV]', len(bin_m1T) - 1, bin_m1T))
variables["fakes_CR"].append(variable('m_o1', 'M_{o1} [GeV]', len(bin_mo1) - 1 , bin_mo1))
variables["fakes_CR"].append(variable('tau_DeepTauVsEle_raw', '#tau DeepTauVsEle raw', 7, array("f", list(np.linspace(-0.3, 1, 8)))))
variables["fakes_CR"].append(variable('tau_DeepTauVsMu_raw', '#tau DeepTauVsMu raw', 7,array("f", list(np.linspace(-0.3, 1, 8)))))
variables["fakes_CR"].append(variable('leadjet_DeepFlv_b', 'leading jet DeepFlavour b raw',len(bin_df["fakes_CR"]) - 1, bin_df["fakes_CR"]))
variables["fakes_CR"].append(variable('subleadjet_DeepFlv_b', 'subleading jet DeepFlavour b raw', len(bin_df["fakes_CR"]) - 1, bin_df["fakes_CR"]))
variables["fakes_CR"].append(variable('lepton_pfRelIso04', 'lepton isolation', 15, array("f", list(np.linspace(0, 0.15, 16)))))
variables["fakes_CR"].append(variable('event_RT', 'R_{T}', len(bin_rt["fakes_CR"]) - 1, bin_rt["fakes_CR"]))
variables["fakes_CR"].append(variable('deltaPhi_jj', '#Delta #phi_{jj}', 14, array("f", list(np.linspace(-3.5, 3.5, 15)))))
variables["fakes_CR"].append(variable('MET_pt', 'p_{T}^{miss} [GeV]', len(bin_metpt["fakes_CR"]) - 1, bin_metpt["fakes_CR"]))
variables["fakes_CR"].append(variable('event_Zeppenfeld_over_deltaEta_jj', 'event Zeppenfeld',  len(bin_zepp) - 1, bin_zepp))
variables["fakes_CR"].append(variable('ptRel_tauj1', 'relative p_{T} #tau j_{1}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["fakes_CR"].append(variable('ptRel_tauj2', 'relative p_{T} #tau j_{2}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["fakes_CR"].append(variable('ptRel_lepj1', 'relative p_{T} #l j_{1}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["fakes_CR"].append(variable('ptRel_lepj2', 'relative p_{T} #l j_{2}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["fakes_CR"].append(variable('deltaEta_jj', '#Delta #eta_{jj}', len(bin_deltaeta_jj) - 1, bin_deltaeta_jj))
variables["fakes_CR"].append(variable('taujet_relpt',  '#tau jet relative p_{T}', len(bin_taujetrelpt) - 1, bin_taujetrelpt))
variables["fakes_CR"].append(variable('mT_lep_MET', 'M_{T}(#l, MET) [GeV]',  len(bin_mTs["fakes_CR"]) - 1, bin_mTs["fakes_CR"]))

variables["ttbar_CR"] = []
variables["ttbar_CR"].append(variable('leadjet_pt',  'Lead jet p_{T} [GeV]', 9 ,array("f", [0., 50., 100., 150., 200., 250., 300., 400., 500., 600.])))
variables["ttbar_CR"].append(variable('subleadjet_pt',  'Sublead jet p_{T} [GeV]', 5 , array("f", [0., 50., 100., 150., 250., 500.])))
variables["ttbar_CR"].append(variable('lepton_pt',  'Lepton p_{T} [GeV]', 9 , array("f", [0., 30., 45., 60., 80., 100., 125., 150, 200., 250.]) ))
variables["ttbar_CR"].append(variable('tau_pt',  'Tau p_{T} [GeV]', 8 , array("f", [30., 45., 60., 80., 100., 125., 150, 200., 250.])))
variables["ttbar_CR"].append(variable('SMbdt', 'SM BDT output',  5, array("f", [0., 0.2, 0.4, 0.6, 0.8, 1.])))
variables["ttbar_CR"].append(variable('m_jj', 'Invarant mass JJ',  6, array("f", [0., 300., 500., 700., 1000., 1500., 2000.])))
variables["ttbar_CR"].append(variable('nJets', 'n jets', 11, array("f", list(np.linspace(-0.5, 10.5, 12)))))
variables["ttbar_CR"].append(variable('nBJets', 'n bjets (DeepJet M)', 6, array("f", list(np.linspace(-0.5, 5.5, 7)))))
variables["ttbar_CR"].append(variable('m_jjtau', 'invariant mass j_{1} j_{2} #tau [GeV]',  len(bin_invm["ttbar_CR"]) - 1, bin_invm["ttbar_CR"]))
variables["ttbar_CR"].append(variable('m_jjtaulep', 'invariant mass j_{1} j_{2} #l #tau [GeV]',  len(bin_invm["ttbar_CR"]) - 1, bin_invm["ttbar_CR"]))
variables["ttbar_CR"].append(variable('m_1T', 'M_{1T} [GeV]', len(bin_m1T) - 1, bin_m1T))
variables["ttbar_CR"].append(variable('m_o1', 'M_{o1} [GeV]', len(bin_mo1) - 1 , bin_mo1))
variables["ttbar_CR"].append(variable('tau_DeepTauVsEle_raw', '#tau DeepTauVsEle raw', 7, array("f", list(np.linspace(-0.3, 1, 8)))))
variables["ttbar_CR"].append(variable('tau_DeepTauVsMu_raw', '#tau DeepTauVsMu raw', 7,array("f", list(np.linspace(-0.3, 1, 8)))))
variables["ttbar_CR"].append(variable('leadjet_DeepFlv_b', 'leading jet DeepFlavour b raw',len(bin_df["ttbar_CR"]) - 1, bin_df["ttbar_CR"]))
variables["ttbar_CR"].append(variable('subleadjet_DeepFlv_b', 'subleading jet DeepFlavour b raw', len(bin_df["ttbar_CR"]) - 1, bin_df["ttbar_CR"]))
variables["ttbar_CR"].append(variable('lepton_pfRelIso04', 'lepton isolation', 15, array("f", list(np.linspace(0, 0.15, 16)))))
variables["ttbar_CR"].append(variable('event_RT', 'R_{T}', len(bin_rt["ttbar_CR"]) - 1, bin_rt["ttbar_CR"]))
variables["ttbar_CR"].append(variable('deltaPhi_jj', '#Delta #phi_{jj}', 14, array("f", list(np.linspace(-3.5, 3.5, 15)))))
variables["ttbar_CR"].append(variable('MET_pt', 'p_{T}^{miss} [GeV]', len(bin_metpt["ttbar_CR"]) - 1, bin_metpt["ttbar_CR"]))
variables["ttbar_CR"].append(variable('event_Zeppenfeld_over_deltaEta_jj', 'event Zeppenfeld',  len(bin_zepp) - 1, bin_zepp))
variables["ttbar_CR"].append(variable('ptRel_tauj1', 'relative p_{T} #tau j_{1}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["ttbar_CR"].append(variable('ptRel_tauj2', 'relative p_{T} #tau j_{2}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["ttbar_CR"].append(variable('ptRel_lepj1', 'relative p_{T} #l j_{1}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["ttbar_CR"].append(variable('ptRel_lepj2', 'relative p_{T} #l j_{2}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["ttbar_CR"].append(variable('deltaEta_jj', '#Delta #eta_{jj}', len(bin_deltaeta_jj) - 1, bin_deltaeta_jj))
variables["ttbar_CR"].append(variable('taujet_relpt',  '#tau jet relative p_{T}', len(bin_taujetrelpt) - 1, bin_taujetrelpt))
variables["ttbar_CR"].append(variable('mT_lep_MET', 'M_{T}(#l, MET) [GeV]',  len(bin_mTs["ttbar_CR"]) - 1, bin_mTs["ttbar_CR"]))

variables["OS_CR_bvetoL"] = []
variables["OS_CR_bvetoL"].append(variable('leadjet_pt',  'Lead jet p_{T} [GeV]', 9 ,array("f", [0., 50., 100., 150., 200., 250., 300., 400., 500., 600.])))
variables["OS_CR_bvetoL"].append(variable('subleadjet_pt',  'Sublead jet p_{T} [GeV]', 5 , array("f", [0., 50., 100., 150., 250., 500.])))
variables["OS_CR_bvetoL"].append(variable('lepton_pt',  'Lepton p_{T} [GeV]', 9 , array("f", [0., 30., 45., 60., 80., 100., 125., 150, 200., 250.]) ))
variables["OS_CR_bvetoL"].append(variable('tau_pt',  'Tau p_{T} [GeV]', 8 , array("f", [30., 45., 60., 80., 100., 125., 150, 200., 250.])))
variables["OS_CR_bvetoL"].append(variable('SMbdt', 'SM BDT output',  5, array("f", [0., 0.2, 0.4, 0.6, 0.8, 1.])))
variables["OS_CR_bvetoL"].append(variable('m_jj', 'Invarant mass JJ',  6, array("f", [0., 300., 500., 700., 1000., 1500., 2000.])))
variables["OS_CR_bvetoL"].append(variable('nJets', 'n jets', 11, array("f", list(np.linspace(-0.5, 10.5, 12)))))
variables["OS_CR_bvetoL"].append(variable('nBJets', 'n bjets (DeepJet M)', 6, array("f", list(np.linspace(-0.5, 5.5, 7)))))
variables["OS_CR_bvetoL"].append(variable('m_jjtau', 'invariant mass j_{1} j_{2} #tau [GeV]',  len(bin_invm["OS_CR_bvetoL"]) - 1, bin_invm["OS_CR_bvetoL"]))
variables["OS_CR_bvetoL"].append(variable('m_jjtaulep', 'invariant mass j_{1} j_{2} #l #tau [GeV]',  len(bin_invm["OS_CR_bvetoL"]) - 1, bin_invm["OS_CR_bvetoL"]))
variables["OS_CR_bvetoL"].append(variable('m_1T', 'M_{1T} [GeV]', len(bin_m1T) - 1, bin_m1T))
variables["OS_CR_bvetoL"].append(variable('m_o1', 'M_{o1} [GeV]', len(bin_mo1) - 1 , bin_mo1))
variables["OS_CR_bvetoL"].append(variable('tau_DeepTauVsEle_raw', '#tau DeepTauVsEle raw', 7, array("f", list(np.linspace(-0.3, 1, 8)))))
variables["OS_CR_bvetoL"].append(variable('tau_DeepTauVsMu_raw', '#tau DeepTauVsMu raw', 7,array("f", list(np.linspace(-0.3, 1, 8)))))
variables["OS_CR_bvetoL"].append(variable('leadjet_DeepFlv_b', 'leading jet DeepFlavour b raw',len(bin_df["OS_CR_bvetoL"]) - 1, bin_df["OS_CR_bvetoL"]))
variables["OS_CR_bvetoL"].append(variable('subleadjet_DeepFlv_b', 'subleading jet DeepFlavour b raw', len(bin_df["OS_CR_bvetoL"]) - 1, bin_df["OS_CR_bvetoL"]))
variables["OS_CR_bvetoL"].append(variable('lepton_pfRelIso04', 'lepton isolation', 15, array("f", list(np.linspace(0, 0.15, 16)))))
variables["OS_CR_bvetoL"].append(variable('event_RT', 'R_{T}', len(bin_rt["OS_CR_bvetoL"]) - 1, bin_rt["OS_CR_bvetoL"]))
variables["OS_CR_bvetoL"].append(variable('deltaPhi_jj', '#Delta #phi_{jj}', 14, array("f", list(np.linspace(-3.5, 3.5, 15)))))
variables["OS_CR_bvetoL"].append(variable('MET_pt', 'p_{T}^{miss} [GeV]', len(bin_metpt["OS_CR_bvetoL"]) - 1, bin_metpt["OS_CR_bvetoL"]))
variables["OS_CR_bvetoL"].append(variable('event_Zeppenfeld_over_deltaEta_jj', 'event Zeppenfeld',  len(bin_zepp) - 1, bin_zepp))
variables["OS_CR_bvetoL"].append(variable('ptRel_tauj1', 'relative p_{T} #tau j_{1}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["OS_CR_bvetoL"].append(variable('ptRel_tauj2', 'relative p_{T} #tau j_{2}',  len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["OS_CR_bvetoL"].append(variable('ptRel_lepj1', 'relative p_{T} #l j_{1}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["OS_CR_bvetoL"].append(variable('ptRel_lepj2', 'relative p_{T} #l j_{2}', len(bin_ptRel_2) - 1, bin_ptRel_2))
variables["OS_CR_bvetoL"].append(variable('deltaEta_jj', '#Delta #eta_{jj}', len(bin_deltaeta_jj) - 1, bin_deltaeta_jj))
variables["OS_CR_bvetoL"].append(variable('taujet_relpt',  '#tau jet relative p_{T}', len(bin_taujetrelpt) - 1, bin_taujetrelpt))
variables["OS_CR_bvetoL"].append(variable('mT_lep_MET', 'M_{T}(#l, MET) [GeV]',  len(bin_mTs["OS_CR_bvetoL"]) - 1, bin_mTs["OS_CR_bvetoL"]))