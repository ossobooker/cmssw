import FWCore.ParameterSet.Config as cms

# import EventFilter.RPCRawToDigi.rpcUnpacker_cfi
# muonRPCDigis = EventFilter.RPCRawToDigi.rpcUnpacker_cfi.rpcunpacker.clone()

from Configuration.Eras.Modifier_run3_RPC_cff import run3_RPC

from EventFilter.RPCRawToDigi.rpcDigiMerger_cff import rpcDigiMerger 
muonRPCDigis = EventFilter.RPCRawToDigi.rpcDigiMerger_cff.rpcDigiMerger.clone()


run3_RPC.toReplaceWith(muonRPCDigis,rpcDigiMerger)


