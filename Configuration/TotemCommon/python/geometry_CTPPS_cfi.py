import FWCore.ParameterSet.Config as cms

#ideal geometry
XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml', 
 	    'Geometry/CMSCommonData/data/extend/cmsextent.xml',
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/PhaseI/beampipe.xml', 
        'Geometry/CMSCommonData/data/cmsBeam.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/ForwardCommonData/data/forward.xml', 
        'Geometry/ForwardCommonData/data/totemRotations.xml', 
        'Geometry/ForwardCommonData/data/totemMaterials.xml', 
        'Geometry/ForwardCommonData/data/totemt1.xml', 
        'Geometry/ForwardCommonData/data/totemt2.xml', 
        'Geometry/ForwardCommonData/data/ionpump.xml', 
        'Geometry/VeryForwardData/data/RP_Box.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_000.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_001.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_002.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_003.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_004.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_005.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_100.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_101.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_102.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_103.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_104.xml',
        'Geometry/VeryForwardData/data/RP_Box/RP_Box_105.xml',
        'Geometry/VeryForwardData/data/RP_Hybrid.xml',
        'Geometry/VeryForwardData/data/RP_Materials.xml',
        'Geometry/VeryForwardData/data/RP_Transformations.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_000.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_001.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_002.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_003.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_004.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_005.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_100.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_101.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_102.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_103.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_104.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_105.xml',
        'Geometry/VeryForwardData/data/RP_Device.xml',
        'Geometry/VeryForwardData/data/RP_Vertical_Device.xml',
        'Geometry/VeryForwardData/data/RP_Horizontal_Device.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Positive_Station.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Negative_Station.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Stations_Assembly.xml',
        'Geometry/VeryForwardData/data/RP_Sensitive_Dets.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Cuts_Per_Region.xml',
        'Geometry/CTPPSCommonData/data/ppstrackerMaterials.xml',
        'Geometry/CTPPSCommonData/data/CTPPSTrackerModule.xml',
        'Geometry/CTPPSSimData/data/CTPPSTrackersens.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Materials.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Transformations.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Horizontal_Pot.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbar.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_A13.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_A24.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_B13.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_B24.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_C13.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_C24.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_D13.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_D24.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_E13.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_E24.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Box_Negative.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Box_Positive.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Negative_Detector_Assembly.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Positive_Detector_Assembly.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Negative_Station.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Positive_Station.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Stations_Assembly.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_XDistance_From_Beam.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Sensitive_Dets.xml'),
    rootNodeName = cms.string('cms:CMSE')
)

# real geometry
TotemRPGeometryESModule = cms.ESProducer("TotemRPGeometryESModule",
    verbosity = cms.untracked.uint32(1)
)