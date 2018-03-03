from warnings import warnpy3k
warnpy3k("the GL module has been removed in Python 3.0", stacklevel=2)
del warnpy3k

NULL = 0
FALSE = 0
TRUE = 1
ATTRIBSTACKDEPTH = 10
VPSTACKDEPTH = 8
MATRIXSTACKDEPTH = 32
NAMESTACKDEPTH = 1025
STARTTAG = -2
ENDTAG = -3
BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7
PUP_CLEAR = 0
PUP_COLOR = 1
PUP_BLACK = 2
PUP_WHITE = 3
NORMALDRAW = 0x010
PUPDRAW = 0x020
OVERDRAW = 0x040
UNDERDRAW = 0x080
CURSORDRAW = 0x100
DUALDRAW = 0x200
PATTERN_16 = 16
PATTERN_32 = 32
PATTERN_64 = 64
PATTERN_16_SIZE = 16
PATTERN_32_SIZE = 64
PATTERN_64_SIZE = 256
SRC_AUTO = 0
SRC_FRONT = 1
SRC_BACK = 2
SRC_ZBUFFER = 3
SRC_PUP = 4
SRC_OVER = 5
SRC_UNDER = 6
SRC_FRAMEGRABBER = 7
BF_ZERO = 0
BF_ONE = 1
BF_DC = 2
BF_SC = 2
BF_MDC = 3
BF_MSC = 3
BF_SA = 4
BF_MSA = 5
BF_DA = 6
BF_MDA = 7
BF_MIN_SA_MDA = 8
AF_NEVER = 0
AF_LESS = 1
AF_EQUAL = 2
AF_LEQUAL = 3
AF_GREATER = 4
AF_NOTEQUAL = 5
AF_GEQUAL = 6
AF_ALWAYS = 7
ZF_NEVER = 0
ZF_LESS = 1
ZF_EQUAL = 2
ZF_LEQUAL = 3
ZF_GREATER = 4
ZF_NOTEQUAL = 5
ZF_GEQUAL = 6
ZF_ALWAYS = 7
ZSRC_DEPTH = 0
ZSRC_COLOR = 1
SMP_OFF = 0x0
SMP_ON = 0x1
SMP_SMOOTHER = 0x2
SML_OFF = 0x0
SML_ON = 0x1
SML_SMOOTHER = 0x2
SML_END_CORRECT = 0x4
PYSM_OFF = 0
PYSM_ON = 1
PYSM_SHRINK = 2
DT_OFF = 0
DT_ON = 1
PUP_NONE = 0
PUP_GREY = 0x1
PUP_BOX = 0x2
PUP_CHECK = 0x4
GLC_OLDPOLYGON = 0
GLC_ZRANGEMAP = 1
GLC_MQUEUERATE = 2
GLC_SOFTATTACH = 3
GLC_MANAGEBG = 4
GLC_SLOWMAPCOLORS = 5
GLC_INPUTCHANGEBUG = 6
GLC_NOBORDERBUG = 7
GLC_SET_VSYNC = 8
GLC_GET_VSYNC = 9
GLC_VSYNC_SLEEP = 10
GLC_COMPATRATE = 15
C16X1 = 0
C16X2 = 1
C32X1 = 2
C32X2 = 3
CCROSS = 4
FLAT = 0
GOURAUD = 1
LO_ZERO = 0x0
LO_AND = 0x1
LO_ANDR = 0x2
LO_SRC = 0x3
LO_ANDI = 0x4
LO_DST = 0x5
LO_XOR = 0x6
LO_OR = 0x7
LO_NOR = 0x8
LO_XNOR = 0x9
LO_NDST = 0xa
LO_ORR = 0xb
LO_NSRC = 0xc
LO_ORI = 0xd
LO_NAND = 0xe
LO_ONE = 0xf
INFOCUSSCRN = -2
ST_KEEP = 0
ST_ZERO = 1
ST_REPLACE = 2
ST_INCR = 3
ST_DECR = 4
ST_INVERT = 5
SF_NEVER = 0
SF_LESS = 1
SF_EQUAL = 2
SF_LEQUAL = 3
SF_GREATER = 4
SF_NOTEQUAL = 5
SF_GEQUAL = 6
SF_ALWAYS = 7
SS_OFF = 0
SS_DEPTH = 1
PYM_FILL = 1
PYM_POINT = 2
PYM_LINE = 3
PYM_HOLLOW = 4
PYM_LINE_FAST = 5
FG_OFF = 0
FG_ON = 1
FG_DEFINE = 2
FG_VTX_EXP = 2
FG_VTX_LIN = 3
FG_PIX_EXP = 4
FG_PIX_LIN = 5
FG_VTX_EXP2 = 6
FG_PIX_EXP2 = 7
PM_SHIFT = 0
PM_EXPAND = 1
PM_C0 = 2
PM_C1 = 3
PM_ADD24 = 4
PM_SIZE = 5
PM_OFFSET = 6
PM_STRIDE = 7
PM_TTOB = 8
PM_RTOL = 9
PM_ZDATA = 10
PM_WARP = 11
PM_RDX = 12
PM_RDY = 13
PM_CDX = 14
PM_CDY = 15
PM_XSTART = 16
PM_YSTART = 17
PM_VO1 = 1000
NAUTO = 0
NNORMALIZE = 1
AC_CLEAR = 0
AC_ACCUMULATE = 1
AC_CLEAR_ACCUMULATE = 2
AC_RETURN = 3
AC_MULT = 4
AC_ADD = 5
CP_OFF = 0
CP_ON = 1
CP_DEFINE = 2
SB_RESET = 0
SB_TRACK = 1
SB_HOLD = 2
RD_FREEZE = 0x00000001
RD_ALPHAONE = 0x00000002
RD_IGNORE_UNDERLAY = 0x00000004
RD_IGNORE_OVERLAY = 0x00000008
RD_IGNORE_PUP = 0x00000010
RD_OFFSCREEN = 0x00000020
GD_XPMAX = 0
GD_YPMAX = 1
GD_XMMAX = 2
GD_YMMAX = 3
GD_ZMIN = 4
GD_ZMAX = 5
GD_BITS_NORM_SNG_RED = 6
GD_BITS_NORM_SNG_GREEN = 7
GD_BITS_NORM_SNG_BLUE = 8
GD_BITS_NORM_DBL_RED = 9
GD_BITS_NORM_DBL_GREEN = 10
GD_BITS_NORM_DBL_BLUE = 11
GD_BITS_NORM_SNG_CMODE = 12
GD_BITS_NORM_DBL_CMODE = 13
GD_BITS_NORM_SNG_MMAP = 14
GD_BITS_NORM_DBL_MMAP = 15
GD_BITS_NORM_ZBUFFER = 16
GD_BITS_OVER_SNG_CMODE = 17
GD_BITS_UNDR_SNG_CMODE = 18
GD_BITS_PUP_SNG_CMODE = 19
GD_BITS_NORM_SNG_ALPHA = 21
GD_BITS_NORM_DBL_ALPHA = 22
GD_BITS_CURSOR = 23
GD_OVERUNDER_SHARED = 24
GD_BLEND = 25
GD_CIFRACT = 26
GD_CROSSHAIR_CINDEX = 27
GD_DITHER = 28
GD_LINESMOOTH_CMODE = 30
GD_LINESMOOTH_RGB = 31
GD_LOGICOP = 33
GD_NSCRNS = 35
GD_NURBS_ORDER = 36
GD_NBLINKS = 37
GD_NVERTEX_POLY = 39
GD_PATSIZE_64 = 40
GD_PNTSMOOTH_CMODE = 41
GD_PNTSMOOTH_RGB = 42
GD_PUP_TO_OVERUNDER = 43
GD_READSOURCE = 44
GD_READSOURCE_ZBUFFER = 48
GD_STEREO = 50
GD_SUBPIXEL_LINE = 51
GD_SUBPIXEL_PNT = 52
GD_SUBPIXEL_POLY = 53
GD_TRIMCURVE_ORDER = 54
GD_WSYS = 55
GD_ZDRAW_GEOM = 57
GD_ZDRAW_PIXELS = 58
GD_SCRNTYPE = 61
GD_TEXTPORT = 62
GD_NMMAPS = 63
GD_FRAMEGRABBER = 64
GD_TIMERHZ = 66
GD_DBBOX = 67
GD_AFUNCTION = 68
GD_ALPHA_OVERUNDER = 69
GD_BITS_ACBUF = 70
GD_BITS_ACBUF_HW = 71
GD_BITS_STENCIL = 72
GD_CLIPPLANES = 73
GD_FOGVERTEX = 74
GD_LIGHTING_TWOSIDE = 76
GD_POLYMODE = 77
GD_POLYSMOOTH = 78
GD_SCRBOX = 79
GD_TEXTURE = 80
GD_FOGPIXEL = 81
GD_TEXTURE_PERSP = 82
GD_MUXPIPES = 83
GD_NOLIMIT = -2
GD_WSYS_NONE = 0
GD_WSYS_4S = 1
GD_SCRNTYPE_WM = 0
GD_SCRNTYPE_NOWM = 1
N_PIXEL_TOLERANCE = 1
N_CULLING = 2
N_DISPLAY = 3
N_ERRORCHECKING = 4
N_SUBDIVISIONS = 5
N_S_STEPS = 6
N_T_STEPS = 7
N_TILES = 8
N_TMP1 = 9
N_TMP2 = 10
N_TMP3 = 11
N_TMP4 = 12
N_TMP5 = 13
N_TMP6 = 14
N_FILL = 1.0
N_OUTLINE_POLY = 2.0
N_OUTLINE_PATCH = 5.0
N_ISOLINE_S = 12.0
N_ST = 0x8
N_STW = 0xd
N_XYZ = 0x4c
N_XYZW = 0x51
N_TEX = 0x88
N_TEXW = 0x8d
N_RGBA = 0xd0
N_RGBAW = 0xd5
N_P2D = 0x8
N_P2DR = 0xd
N_V3D = 0x4c
N_V3DR = 0x51
N_T2D = 0x88
N_T2DR = 0x8d
N_C4D = 0xd0
N_C4DR = 0xd5
LMNULL = 0.0
MSINGLE = 0
MPROJECTION = 1
MVIEWING = 2
MTEXTURE = 3
MAXLIGHTS = 8
MAXRESTRICTIONS = 4
DEFMATERIAL = 0
EMISSION = 1
AMBIENT = 2
DIFFUSE = 3
SPECULAR = 4
SHININESS = 5
COLORINDEXES = 6
ALPHA = 7
DEFLIGHT = 100
LCOLOR = 101
POSITION = 102
SPOTDIRECTION = 103
SPOTLIGHT = 104
DEFLMODEL = 200
LOCALVIEWER = 201
ATTENUATION = 202
ATTENUATION2 = 203
TWOSIDE = 204
MATERIAL = 1000
BACKMATERIAL = 1001
LIGHT0 = 1100
LIGHT1 = 1101
LIGHT2 = 1102
LIGHT3 = 1103
LIGHT4 = 1104
LIGHT5 = 1105
LIGHT6 = 1106
LIGHT7 = 1107
LMODEL = 1200
LMC_COLOR = 0
LMC_EMISSION = 1
LMC_AMBIENT = 2
LMC_DIFFUSE = 3
LMC_SPECULAR = 4
LMC_AD = 5
LMC_NULL = 6
TX_MINFILTER = 0x100
TX_MAGFILTER = 0x200
TX_WRAP = 0x300
TX_WRAP_S = 0x310
TX_WRAP_T = 0x320
TX_TILE = 0x400
TX_BORDER = 0x500
TX_NULL = 0x000
TX_POINT = 0x110
TX_BILINEAR = 0x220
TX_MIPMAP = 0x120
TX_MIPMAP_POINT = 0x121
TX_MIPMAP_LINEAR = 0x122
TX_MIPMAP_BILINEAR = 0x123
TX_MIPMAP_TRILINEAR = 0x124
TX_REPEAT = 0x301
TX_CLAMP = 0x302
TX_SELECT = 0x303
TX_TEXTURE_0 = 0
TV_MODULATE = 0x101
TV_BLEND = 0x102
TV_DECAL = 0x103
TV_COLOR = 0x200
TV_NULL = 0x000
TV_ENV0 = 0
TX_S = 0
TX_T = 1
TG_OFF = 0
TG_ON = 1
TG_CONTOUR = 2
TG_LINEAR = 3
TG_SPHEREMAP = 4
TG_REFRACTMAP = 5
DGLSINK = 0
DGLLOCAL = 1
DGLTSOCKET = 2
DGL4DDN = 3
PUP_CURSOR = PUP_COLOR
FATAL = 1
WARNING = 2
ASK_CONT = 3
ASK_RESTART = 4
XMAXSCREEN = 1279
YMAXSCREEN = 1023
XMAXMEDIUM = 1023
YMAXMEDIUM = 767
XMAX170 = 645
YMAX170 = 484
XMAXPAL = 779
YMAXPAL = 574
