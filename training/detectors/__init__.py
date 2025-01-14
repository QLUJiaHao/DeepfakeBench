from utils.registry import DETECTOR
from .facexray_detector import FaceXrayDetector
from .xception_detector import XceptionDetector
from .efficientnetb4_detector import EfficientDetector
from .resnet34_detector import ResnetDetector
from .f3net_detector import F3netDetector
from .meso4_detector import Meso4Detector
from .meso4Inception_detector import Meso4InceptionDetector
from .spsl_detector import SpslDetector
from .core_detector import CoreDetector
from .capsule_net_detector import CapsuleNetDetector
from .srm_detector import SRMDetector
from .ucf_detector import UCFDetector
from .recce_detector import RecceDetector
from .fwa_detector import FWADetector
from .ffd_detector import FFDDetector
from .nbmsnlc.baseline import Baseline
from .nbmsnlc.baseline_ms import BaselineMs
# from .nbmsnlc_detector import NBMSNLCDetector
# from .rgbmsnlc_detector import RGBMSNLCDetector
from .efficientnetb4_only import EfficientOnlyDetector