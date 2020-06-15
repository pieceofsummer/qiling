#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org)

# Table from: https://github.com/zeropointdynamics/zelos/blob/master/src/zelos/ext/platforms/linux/syscalls/syscalls_table.py
# cols = ("arm64", "arm", "x86_64", "x32", "x86", "mips", "powerpc", "ia64")

from qiling.const import *

def map_syscall(ql, syscall_num):
    for k,v in syscall_table.items():
        
        if ql.archtype == QL_ARCH.ARM64 and v[0] == syscall_num:
            return "ql_syscall_" + k

        elif ql.archtype == QL_ARCH.ARM and v[1] == syscall_num:
            return "ql_syscall_" + k

        elif ql.archtype == QL_ARCH.X8664 and v[2] == syscall_num:
            return "ql_syscall_" + k

        elif ql.archtype == QL_ARCH.X86 and v[4] == syscall_num:
            return "ql_syscall_" + k            

        elif ql.archtype == QL_ARCH.MIPS and v[5] == syscall_num:
            return "ql_syscall_" + k              

syscall_table = {
    "_llseek": (-1, 140, -1, -1, 140, 4140, 140, -1),
    "_newselect": (-1, 142, -1, -1, 142, 4142, 142, -1),
    "_sysctl": (-1, 149, 156, -1, 149, 4153, 149, 1150),
    "accept": (202, 285, 43, 1073741867, -1, 4168, 330, 1194),
    "accept4": (242, 366, 288, 1073742112, 364, 4334, 344, 1334),
    "access": (-1, 33, 21, 1073741845, 33, 4033, 33, 1049),
    "acct": (89, 51, 163, 1073741987, 51, 4051, 51, 1064),
    "add_key": (217, 309, 248, 1073742072, 286, 4280, 269, 1271),
    "adjtimex": (171, 124, 159, 1073741983, 124, 4124, 124, 1131),
    "afs_syscall": (-1, -1, 183, 1073742007, 137, 4137, 137, 1141),
    "alarm": (-1, -1, 37, 1073741861, 27, 4027, 27, -1),
    "arch_prctl": (-1, -1, 158, 1073741982, 384, -1, -1, -1),
    "arm_fadvise64_64": (-1, 270, -1, -1, -1, -1, -1, -1),
    "arm_sync_file_range": (-1, 341, -1, -1, -1, -1, -1, -1),
    "bdflush": (-1, 134, -1, -1, 134, 4134, 134, 1138),
    "bind": (200, 282, 49, 1073741873, 361, 4169, 327, 1191),
    "bpf": (280, 386, 321, 1073742145, 357, 4355, 361, 1341),
    "break": (-1, -1, -1, -1, 17, 4017, 17, -1),
    "brk": (214, 45, 12, 1073741836, 45, 4045, 45, 1060),
    "cachectl": (-1, -1, -1, -1, -1, 4148, -1, -1),
    # Modified cacheflush arm -1 -> 983042
    "cacheflush": (-1, 983042, -1, -1, -1, 4147, -1, -1),
    "capget": (90, 184, 125, 1073741949, 184, 4204, 183, 1185),
    "capset": (91, 185, 126, 1073741950, 185, 4205, 184, 1186),
    "chdir": (49, 12, 80, 1073741904, 12, 4012, 12, 1034),
    "chmod": (-1, 15, 90, 1073741914, 15, 4015, 15, 1038),
    "chown": (-1, 182, 92, 1073741916, 182, 4202, 181, 1039),
    "chown32": (-1, 212, -1, -1, 212, -1, -1, -1),
    "chroot": (51, 61, 161, 1073741985, 61, 4061, 61, 1068),
    "clock_adjtime": (266, 372, 305, 1073742129, 343, 4341, 347, 1328),
    "clock_adjtime64": (-1, 405, -1, -1, 405, 4405, 405, -1),
    "clock_getres": (114, 264, 229, 1073742053, 266, 4264, 247, 1255),
    "clock_getres_time64": (-1, 406, -1, -1, 406, 4406, 406, -1),
    "clock_gettime": (113, 263, 228, 1073742052, 265, 4263, 246, 1254),
    "clock_gettime64": (-1, 403, -1, -1, 403, 4403, 403, -1),
    "clock_nanosleep": (115, 265, 230, 1073742054, 267, 4265, 248, 1256),
    "clock_nanosleep_time64": (-1, 407, -1, -1, 407, 4407, 407, -1),
    "clock_settime": (112, 262, 227, 1073742051, 264, 4262, 245, 1253),
    "clock_settime64": (-1, 404, -1, -1, 404, 4404, 404, -1),
    "clone": (220, 120, 56, 1073741880, 120, 4120, 120, 1128),
    "clone2": (-1, -1, -1, -1, -1, -1, -1, 1213),
    "close": (57, 6, 3, 1073741827, 6, 4006, 6, 1029),
    "connect": (203, 283, 42, 1073741866, 362, 4170, 328, 1192),
    "copy_file_range": (285, 391, 326, 1073742150, 377, 4360, 379, 1347),
    "creat": (-1, 8, 85, 1073741909, 8, 4008, 8, 1030),
    "create_module": (-1, -1, 174, -1, 127, 4127, 127, -1),
    "delete_module": (106, 129, 176, 1073742000, 129, 4129, 129, 1134),
    "dup": (23, 41, 32, 1073741856, 41, 4041, 41, 1057),
    "dup2": (-1, 63, 33, 1073741857, 63, 4063, 63, 1070),
    "dup3": (24, 358, 292, 1073742116, 330, 4327, 316, 1316),
    "epoll_create": (-1, 250, 213, 1073742037, 254, 4248, 236, 1243),
    "epoll_create1": (20, 357, 291, 1073742115, 329, 4326, 315, 1315),
    "epoll_ctl": (21, 251, 233, 1073742057, 255, 4249, 237, 1244),
    "epoll_ctl_old": (-1, -1, 214, -1, -1, -1, -1, -1),
    "epoll_pwait": (22, 346, 281, 1073742105, 319, 4313, 303, 1305),
    "epoll_wait": (-1, 252, 232, 1073742056, 256, 4250, 238, 1245),
    "epoll_wait_old": (-1, -1, 215, -1, -1, -1, -1, -1),
    "eventfd": (-1, 351, 284, 1073742108, 323, 4319, 307, 1309),
    "eventfd2": (19, 356, 290, 1073742114, 328, 4325, 314, 1314),
    "execve": (221, 11, 59, 1073742344, 11, 4011, 11, 1033),
    "execveat": (281, 387, 322, 1073742369, 358, 4356, 362, 1342),
    "exit": (93, 1, 60, 1073741884, 1, 4001, 1, 1025),
    "exit_group": (94, 248, 231, 1073742055, 252, 4246, 234, 1236),
    "faccessat": (48, 334, 269, 1073742093, 307, 4300, 298, 1293),
    "fadvise64": (223, -1, 221, 1073742045, 250, 4254, 233, 1234),
    "fadvise64_64": (-1, -1, -1, -1, 272, -1, 254, -1),
    "fallocate": (47, 352, 285, 1073742109, 324, 4320, 309, 1303),
    "fanotify_init": (262, 367, 300, 1073742124, 338, 4336, 323, 1323),
    "fanotify_mark": (263, 368, 301, 1073742125, 339, 4337, 324, 1324),
    "fchdir": (50, 133, 81, 1073741905, 133, 4133, 133, 1035),
    "fchmod": (52, 94, 91, 1073741915, 94, 4094, 94, 1099),
    "fchmodat": (53, 333, 268, 1073742092, 306, 4299, 297, 1292),
    "fchown": (55, 95, 93, 1073741917, 95, 4095, 95, 1100),
    "fchown32": (-1, 207, -1, -1, 207, -1, -1, -1),
    "fchownat": (54, 325, 260, 1073742084, 298, 4291, 289, 1284),
    "fcntl": (25, 55, 72, 1073741896, 55, 4055, 55, 1066),
    "fcntl64": (-1, 221, -1, -1, 221, 4220, 204, -1),
    "fdatasync": (83, 148, 75, 1073741899, 148, 4152, 148, 1052),
    "fgetxattr": (10, 231, 193, 1073742017, 231, 4229, 214, 1222),
    "finit_module": (273, 379, 313, 1073742137, 350, 4348, 353, 1335),
    "flistxattr": (13, 234, 196, 1073742020, 234, 4232, 217, 1225),
    "flock": (32, 143, 73, 1073741897, 143, 4143, 143, 1145),
    "fork": (-1, 2, 57, 1073741881, 2, 4002, 2, -1),
    "fremovexattr": (16, 237, 199, 1073742023, 237, 4235, 220, 1228),
    "fsconfig": (431, 431, 431, 1073742255, 431, 4431, 431, 1455),
    "fsetxattr": (7, 228, 190, 1073742014, 228, 4226, 211, 1219),
    "fsmount": (432, 432, 432, 1073742256, 432, 4432, 432, 1456),
    "fsopen": (430, 430, 430, 1073742254, 430, 4430, 430, 1454),
    "fspick": (433, 433, 433, 1073742257, 433, 4433, 433, 1457),
    "fstat": (80, 108, 5, 1073741829, 108, 4108, 108, 1212),
    "fstat64": (-1, 197, -1, -1, 197, 4215, 197, -1),
    "fstatat64": (-1, 327, -1, -1, 300, 4293, 291, -1),
    "fstatfs": (44, 100, 138, 1073741962, 100, 4100, 100, 1104),
    "fstatfs64": (-1, 267, -1, -1, 269, 4256, 253, 1257),
    "fsync": (82, 118, 74, 1073741898, 118, 4118, 118, 1051),
    "ftime": (-1, -1, -1, -1, 35, 4035, 35, -1),
    "ftruncate": (46, 93, 77, 1073741901, 93, 4093, 93, 1098),
    "ftruncate64": (-1, 194, -1, -1, 194, 4212, 194, -1),
    "futex": (98, 240, 202, 1073742026, 240, 4238, 221, 1230),
    "futex_time64": (-1, 422, -1, -1, 422, 4422, 422, -1),
    "futimesat": (-1, 326, 261, 1073742085, 299, 4292, 290, 1285),
    "get_kernel_syms": (-1, -1, 177, -1, 130, 4130, 130, -1),
    "get_mempolicy": (236, 320, 239, 1073742063, 275, 4269, 260, 1260),
    "get_robust_list": (100, 339, 274, 1073742355, 312, 4310, 299, 1299),
    "get_thread_area": (-1, -1, 211, -1, 244, -1, -1, -1),
    "getcpu": (168, 345, 309, 1073742133, 318, 4312, 302, 1304),
    "getcwd": (17, 183, 79, 1073741903, 183, 4203, 182, 1184),
    "getdents": (-1, 141, 78, 1073741902, 141, 4141, 141, 1144),
    "getdents64": (61, 217, 217, 1073742041, 220, 4219, 202, 1214),
    "getegid": (177, 50, 108, 1073741932, 50, 4050, 50, 1063),
    "getegid32": (-1, 202, -1, -1, 202, -1, -1, -1),
    "geteuid": (175, 49, 107, 1073741931, 49, 4049, 49, 1047),
    "geteuid32": (-1, 201, -1, -1, 201, -1, -1, -1),
    "getgid": (176, 47, 104, 1073741928, 47, 4047, 47, 1062),
    "getgid32": (-1, 200, -1, -1, 200, -1, -1, -1),
    "getgroups": (158, 80, 115, 1073741939, 80, 4080, 80, 1077),
    "getgroups32": (-1, 205, -1, -1, 205, -1, -1, -1),
    "getitimer": (102, 105, 36, 1073741860, 105, 4105, 105, 1119),
    "getpeername": (205, 287, 52, 1073741876, 368, 4171, 332, 1196),
    "getpgid": (155, 132, 121, 1073741945, 132, 4132, 132, 1079),
    "getpgrp": (-1, 65, 111, 1073741935, 65, 4065, 65, -1),
    "getpid": (172, 20, 39, 1073741863, 20, 4020, 20, 1041),
    "getpmsg": (-1, -1, 181, 1073742005, 188, 4208, 187, 1188),
    "getppid": (173, 64, 110, 1073741934, 64, 4064, 64, 1042),
    "getpriority": (141, 96, 140, 1073741964, 96, 4096, 96, 1101),
    "getrandom": (278, 384, 318, 1073742142, 355, 4353, 359, 1339),
    "getresgid": (150, 171, 120, 1073741944, 171, 4191, 170, 1075),
    "getresgid32": (-1, 211, -1, -1, 211, -1, -1, -1),
    "getresuid": (148, 165, 118, 1073741942, 165, 4186, 165, 1073),
    "getresuid32": (-1, 209, -1, -1, 209, -1, -1, -1),
    "getrlimit": (163, -1, 97, 1073741921, 76, 4076, 76, 1085),
    "getrusage": (165, 77, 98, 1073741922, 77, 4077, 77, 1086),
    "getsid": (156, 147, 124, 1073741948, 147, 4151, 147, 1082),
    "getsockname": (204, 286, 51, 1073741875, 367, 4172, 331, 1195),
    "getsockopt": (209, 295, 55, 1073742366, 365, 4173, 340, 1204),
    "gettid": (178, 224, 186, 1073742010, 224, 4222, 207, 1105),
    "gettimeofday": (169, 78, 96, 1073741920, 78, 4078, 78, 1087),
    "getuid": (174, 24, 102, 1073741926, 24, 4024, 24, 1046),
    "getuid32": (-1, 199, -1, -1, 199, -1, -1, -1),
    "getunwind": (-1, -1, -1, -1, -1, -1, -1, 1215),
    "getxattr": (8, 229, 191, 1073742015, 229, 4227, 212, 1220),
    "gtty": (-1, -1, -1, -1, 32, 4032, 32, -1),
    "idle": (-1, -1, -1, -1, 112, 4112, 112, -1),
    "init_module": (105, 128, 175, 1073741999, 128, 4128, 128, 1133),
    "inotify_add_watch": (27, 317, 254, 1073742078, 292, 4285, 276, 1278),
    "inotify_init": (-1, 316, 253, 1073742077, 291, 4284, 275, 1277),
    "inotify_init1": (26, 360, 294, 1073742118, 332, 4329, 318, 1318),
    "inotify_rm_watch": (28, 318, 255, 1073742079, 293, 4286, 277, 1279),
    "io_cancel": (3, 247, 210, 1073742034, 249, 4245, 231, 1242),
    "io_destroy": (1, 244, 207, 1073742031, 246, 4242, 228, 1239),
    "io_getevents": (4, 245, 208, 1073742032, 247, 4243, 229, 1240),
    "io_pgetevents": (292, 399, 333, 1073742157, 385, 4368, 388, 1351),
    "io_pgetevents_time64": (-1, 416, -1, -1, 416, 4416, 416, -1),
    "io_setup": (0, 243, 206, 1073742367, 245, 4241, 227, 1238),
    "io_submit": (2, 246, 209, 1073742368, 248, 4244, 230, 1241),
    "io_uring_enter": (426, 426, 426, 1073742250, 426, 4426, 426, 1450),
    "io_uring_register": (427, 427, 427, 1073742251, 427, 4427, 427, 1451),
    "io_uring_setup": (425, 425, 425, 1073742249, 425, 4425, 425, 1449),
    "ioctl": (29, 54, 16, 1073742338, 54, 4054, 54, 1065),
    "ioperm": (-1, -1, 173, 1073741997, 101, 4101, 101, -1),
    "iopl": (-1, -1, 172, 1073741996, 110, 4110, 110, -1),
    "ioprio_get": (31, 315, 252, 1073742076, 290, 4315, 274, 1275),
    "ioprio_set": (30, 314, 251, 1073742075, 289, 4314, 273, 1274),
    "ipc": (-1, -1, -1, -1, 117, 4117, 117, -1),
    "kcmp": (272, 378, 312, 1073742136, 349, 4347, 354, 1345),
    "kexec_file_load": (294, 401, 320, 1073742144, -1, -1, 382, -1),
    "kexec_load": (104, 347, 246, 1073742352, 283, 4311, 268, 1268),
    "keyctl": (219, 311, 250, 1073742074, 288, 4282, 271, 1273),
    "kill": (129, 37, 62, 1073741886, 37, 4037, 37, 1053),
    "lchown": (-1, 16, 94, 1073741918, 16, 4016, 16, 1124),
    "lchown32": (-1, 198, -1, -1, 198, -1, -1, -1),
    "lgetxattr": (9, 230, 192, 1073742016, 230, 4228, 213, 1221),
    "link": (-1, 9, 86, 1073741910, 9, 4009, 9, 1031),
    "linkat": (37, 330, 265, 1073742089, 303, 4296, 294, 1289),
    "listen": (201, 284, 50, 1073741874, 363, 4174, 329, 1193),
    "listxattr": (11, 232, 194, 1073742018, 232, 4230, 215, 1223),
    "llistxattr": (12, 233, 195, 1073742019, 233, 4231, 216, 1224),
    "lock": (-1, -1, -1, -1, 53, 4053, 53, -1),
    "lookup_dcookie": (18, 249, 212, 1073742036, 253, 4247, 235, 1237),
    "lremovexattr": (15, 236, 198, 1073742022, 236, 4234, 219, 1227),
    "lseek": (62, 19, 8, 1073741832, 19, 4019, 19, 1040),
    "lsetxattr": (6, 227, 189, 1073742013, 227, 4225, 210, 1218),
    "lstat": (-1, 107, 6, 1073741830, 107, 4107, 107, 1211),
    "lstat64": (-1, 196, -1, -1, 196, 4214, 196, -1),
    "madvise": (233, 220, 28, 1073741852, 219, 4218, 205, 1209),
    "mbind": (235, 319, 237, 1073742061, 274, 4268, 259, 1259),
    "membarrier": (283, 389, 324, 1073742148, 375, 4358, 365, 1344),
    "memfd_create": (279, 385, 319, 1073742143, 356, 4354, 360, 1340),
    "migrate_pages": (238, 400, 256, 1073742080, 294, 4287, 258, 1280),
    "mincore": (232, 219, 27, 1073741851, 218, 4217, 206, 1208),
    "mkdir": (-1, 39, 83, 1073741907, 39, 4039, 39, 1055),
    "mkdirat": (34, 323, 258, 1073742082, 296, 4289, 287, 1282),
    "mknod": (-1, 14, 133, 1073741957, 14, 4014, 14, 1037),
    "mknodat": (33, 324, 259, 1073742083, 297, 4290, 288, 1283),
    "mlock": (228, 150, 149, 1073741973, 150, 4154, 150, 1153),
    "mlock2": (284, 390, 325, 1073742149, 376, 4359, 378, 1346),
    "mlockall": (230, 152, 151, 1073741975, 152, 4156, 152, 1154),
    "mmap": (222, -1, 9, 1073741833, 90, 4090, 90, 1151),
    "mmap2": (-1, 192, -1, -1, 192, 4210, 192, 1172),
    "modify_ldt": (-1, -1, 154, 1073741978, 123, 4123, 123, -1),
    "mount": (40, 21, 165, 1073741989, 21, 4021, 21, 1043),
    "move_mount": (429, 429, 429, 1073742253, 429, 4429, 429, 1453),
    "move_pages": (239, 344, 279, 1073742357, 317, 4308, 301, 1276),
    "mprotect": (226, 125, 10, 1073741834, 125, 4125, 125, 1155),
    "mpx": (-1, -1, -1, -1, 56, 4056, 56, -1),
    "mq_getsetattr": (185, 279, 245, 1073742069, 282, 4276, 267, 1267),
    "mq_notify": (184, 278, 244, 1073742351, 281, 4275, 266, 1266),
    "mq_open": (180, 274, 240, 1073742064, 277, 4271, 262, 1262),
    "mq_timedreceive": (183, 277, 243, 1073742067, 280, 4274, 265, 1265),
    "mq_timedreceive_time64": (-1, 419, -1, -1, 419, 4419, 419, -1),
    "mq_timedsend": (182, 276, 242, 1073742066, 279, 4273, 264, 1264),
    "mq_timedsend_time64": (-1, 418, -1, -1, 418, 4418, 418, -1),
    "mq_unlink": (181, 275, 241, 1073742065, 278, 4272, 263, 1263),
    "mremap": (216, 163, 25, 1073741849, 163, 4167, 163, 1156),
    "msgctl": (187, 304, 71, 1073741895, 402, 4402, 402, 1112),
    "msgget": (186, 303, 68, 1073741892, 399, 4399, 399, 1109),
    "msgrcv": (188, 302, 70, 1073741894, 401, 4401, 401, 1111),
    "msgsnd": (189, 301, 69, 1073741893, 400, 4400, 400, 1110),
    "msync": (227, 144, 26, 1073741850, 144, 4144, 144, 1157),
    "multiplexer": (-1, -1, -1, -1, -1, -1, 201, -1),
    "munlock": (229, 151, 150, 1073741974, 151, 4155, 151, 1158),
    "munlockall": (231, 153, 152, 1073741976, 153, 4157, 153, 1159),
    "munmap": (215, 91, 11, 1073741835, 91, 4091, 91, 1152),
    "name_to_handle_at": (264, 370, 303, 1073742127, 341, 4339, 345, 1326),
    "nanosleep": (101, 162, 35, 1073741859, 162, 4166, 162, 1168),
    "fstatat64": (79, -1, 262, 1073742086, -1, -1, -1, 1286),
    "nfsservctl": (42, 169, 180, -1, 169, 4189, 168, 1169),
    "ni_syscall": (-1, -1, -1, -1, -1, -1, -1, 1024),
    "nice": (-1, 34, -1, -1, 34, 4034, 34, -1),
    "oldfstat": (-1, -1, -1, -1, 28, -1, 28, -1),
    "oldlstat": (-1, -1, -1, -1, 84, -1, 84, -1),
    "oldolduname": (-1, -1, -1, -1, 59, -1, 59, -1),
    "oldstat": (-1, -1, -1, -1, 18, -1, 18, -1),
    "olduname": (-1, -1, -1, -1, 109, -1, 109, -1),
    "open": (-1, 5, 2, 1073741826, 5, 4005, 5, 1028),
    "open_by_handle_at": (265, 371, 304, 1073742128, 342, 4340, 346, 1327),
    "open_tree": (428, 428, 428, 1073742252, 428, 4428, 428, 1452),
    "openat": (56, 322, 257, 1073742081, 295, 4288, 286, 1281),
    "pause": (-1, 29, 34, 1073741858, 29, 4029, 29, -1),
    "pciconfig_iobase": (-1, 271, -1, -1, -1, -1, 200, -1),
    "pciconfig_read": (-1, 272, -1, -1, -1, -1, 198, 1173),
    "pciconfig_write": (-1, 273, -1, -1, -1, -1, 199, 1174),
    "perf_event_open": (241, 364, 298, 1073742122, 336, 4333, 319, 1352),
    "perfmonctl": (-1, -1, -1, -1, -1, -1, -1, 1175),
    "personality": (92, 136, 135, 1073741959, 136, 4136, 136, 1140),
    "pidfd_send_signal": (424, 424, 424, 1073742248, 424, 4424, 424, 1448),
    "pipe": (-1, 42, 22, 1073741846, 42, 4042, 42, 1058),
    "pipe2": (59, 359, 293, 1073742117, 331, 4328, 317, 1317),
    "pivot_root": (41, 218, 155, 1073741979, 217, 4216, 203, 1207),
    "pkey_alloc": (289, 395, 330, 1073742154, 381, 4364, 384, 1355),
    "pkey_free": (290, 396, 331, 1073742155, 382, 4365, 385, 1356),
    "pkey_mprotect": (288, 394, 329, 1073742153, 380, 4363, 386, 1354),
    "poll": (-1, 168, 7, 1073741831, 168, 4188, 167, 1090),
    "ppoll": (73, 336, 271, 1073742095, 309, 4302, 281, 1295),
    "ppoll_time64": (-1, 414, -1, -1, 414, 4414, 414, -1),
    "prctl": (167, 172, 157, 1073741981, 172, 4192, 171, 1170),
    "pread64": (67, 180, 17, 1073741841, 180, 4200, 179, 1148),
    "preadv": (69, 361, 295, 1073742358, 333, 4330, 320, 1319),
    "preadv2": (286, 392, 327, 1073742370, 378, 4361, 380, 1348),
    "prlimit64": (261, 369, 302, 1073742126, 340, 4338, 325, 1325),
    "process_vm_readv": (270, 376, 310, 1073742363, 347, 4345, 351, 1332),
    "process_vm_writev": (271, 377, 311, 1073742364, 348, 4346, 352, 1333),
    "prof": (-1, -1, -1, -1, 44, 4044, 44, -1),
    "profil": (-1, -1, -1, -1, 98, 4098, 98, -1),
    "pselect6": (72, 335, 270, 1073742094, 308, 4301, 280, 1294),
    "pselect6_time64": (-1, 413, -1, -1, 413, 4413, 413, -1),
    "ptrace": (117, 26, 101, 1073742345, 26, 4026, 26, 1048),
    "putpmsg": (-1, -1, 182, 1073742006, 189, 4209, 188, 1189),
    "pwrite64": (68, 181, 18, 1073741842, 181, 4201, 180, 1149),
    "pwritev": (70, 362, 296, 1073742359, 334, 4331, 321, 1320),
    "pwritev2": (287, 393, 328, 1073742371, 379, 4362, 381, 1349),
    "query_module": (-1, -1, 178, -1, 167, 4187, 166, -1),
    "quotactl": (60, 131, 179, 1073742003, 131, 4131, 131, 1137),
    "read": (63, 3, 0, 1073741824, 3, 4003, 3, 1026),
    "readahead": (213, 225, 187, 1073742011, 225, 4223, 191, 1216),
    "readdir": (-1, -1, -1, -1, 89, 4089, 89, -1),
    "readlink": (-1, 85, 89, 1073741913, 85, 4085, 85, 1092),
    "readlinkat": (78, 332, 267, 1073742091, 305, 4298, 296, 1291),
    "readv": (65, 145, 19, 1073742339, 145, 4145, 145, 1146),
    "reboot": (142, 88, 169, 1073741993, 88, 4088, 88, 1096),
    "recv": (-1, 291, -1, -1, -1, 4175, 336, 1200),
    "recvfrom": (207, 292, 45, 1073742341, 371, 4176, 337, 1201),
    "recvmmsg": (243, 365, 299, 1073742361, 337, 4335, 343, 1322),
    "recvmmsg_time64": (-1, 417, -1, -1, 417, 4417, 417, -1),
    "recvmsg": (212, 297, 47, 1073742343, 372, 4177, 342, 1206),
    "remap_file_pages": (234, 253, 216, 1073742040, 257, 4251, 239, 1125),
    "removexattr": (14, 235, 197, 1073742021, 235, 4233, 218, 1226),
    "rename": (-1, 38, 82, 1073741906, 38, 4038, 38, 1054),
    "renameat": (38, 329, 264, 1073742088, 302, 4295, 293, 1288),
    "renameat2": (276, 382, 316, 1073742140, 353, 4351, 357, 1338),
    "request_key": (218, 310, 249, 1073742073, 287, 4281, 270, 1272),
    "restart_syscall": (128, 0, 219, 1073742043, 0, 4253, 0, 1246),
    "rmdir": (-1, 40, 84, 1073741908, 40, 4040, 40, 1056),
    "rseq": (293, 398, 334, 1073742158, 386, 4367, 387, 1357),
    "rt_sigaction": (134, 174, 13, 1073742336, 174, 4194, 173, 1177),
    "rt_sigpending": (136, 176, 127, 1073742346, 176, 4196, 175, 1178),
    "rt_sigprocmask": (135, 175, 14, 1073741838, 175, 4195, 174, 1179),
    "rt_sigqueueinfo": (138, 178, 129, 1073742348, 178, 4198, 177, 1180),
    "rt_sigreturn": (139, 173, 15, 1073742337, 173, 4193, 172, 1181),
    "rt_sigsuspend": (133, 179, 130, 1073741954, 179, 4199, 178, 1182),
    "rt_sigtimedwait": (137, 177, 128, 1073742347, 177, 4197, 176, 1183),
    "rt_sigtimedwait_time64": (-1, 421, -1, -1, 421, 4421, 421, -1),
    "rt_tgsigqueueinfo": (240, 363, 297, 1073742360, 335, 4332, 322, 1321),
    "rtas": (-1, -1, -1, -1, -1, -1, 255, -1),
    "sched_get_priority_max": (
        125,
        159,
        146,
        1073741970,
        159,
        4163,
        159,
        1165,
    ),
    "sched_get_priority_min": (
        126,
        160,
        147,
        1073741971,
        160,
        4164,
        160,
        1166,
    ),
    "sched_getaffinity": (123, 242, 204, 1073742028, 242, 4240, 223, 1232),
    "sched_getattr": (275, 381, 315, 1073742139, 352, 4350, 356, 1337),
    "sched_getparam": (121, 155, 143, 1073741967, 155, 4159, 155, 1160),
    "sched_getscheduler": (120, 157, 145, 1073741969, 157, 4161, 157, 1162),
    "sched_rr_get_interval": (127, 161, 148, 1073741972, 161, 4165, 161, 1167),
    "sched_rr_get_interval_time64": (-1, 423, -1, -1, 423, 4423, 423, -1),
    "sched_setaffinity": (122, 241, 203, 1073742027, 241, 4239, 222, 1231),
    "sched_setattr": (274, 380, 314, 1073742138, 351, 4349, 355, 1336),
    "sched_setparam": (118, 154, 142, 1073741966, 154, 4158, 154, 1161),
    "sched_setscheduler": (119, 156, 144, 1073741968, 156, 4160, 156, 1163),
    "sched_yield": (124, 158, 24, 1073741848, 158, 4162, 158, 1164),
    "seccomp": (277, 383, 317, 1073742141, 354, 4352, 358, 1353),
    "security": (-1, -1, 185, 1073742009, -1, -1, -1, -1),
    "select": (-1, -1, 23, 1073741847, 82, -1, 82, 1089),
    "semctl": (191, 300, 66, 1073741890, 394, 4394, 394, 1108),
    "semget": (190, 299, 64, 1073741888, 393, 4393, 393, 1106),
    "semop": (193, 298, 65, 1073741889, -1, -1, -1, 1107),
    "semtimedop": (192, 312, 220, 1073742044, -1, -1, -1, 1247),
    "semtimedop_time64": (-1, 420, -1, -1, 420, 4420, 420, -1),
    "send": (-1, 289, -1, -1, -1, 4178, 334, 1198),
    "sendfile": (71, 187, 40, 1073741864, 187, 4207, 186, 1187),
    "sendfile64": (-1, 239, -1, -1, 239, 4237, 226, -1),
    "sendmmsg": (269, 374, 307, 1073742362, 345, 4343, 349, 1331),
    "sendmsg": (211, 296, 46, 1073742342, 370, 4179, 341, 1205),
    "sendto": (206, 290, 44, 1073741868, 369, 4180, 335, 1199),
    "set_mempolicy": (237, 321, 238, 1073742062, 276, 4270, 261, 1261),
    "set_robust_list": (99, 338, 273, 1073742354, 311, 4309, 300, 1298),
    "set_thread_area": (-1, -1, 205, -1, 243, 4283, -1, -1),
    "set_tid_address": (96, 256, 218, 1073742042, 258, 4252, 232, 1233),
    # Custom arm syscall set_tls.
    "set_tls": (-1, 0xF0005, -1, -1, -1, -1, -1, -1),
    "setdomainname": (162, 121, 171, 1073741995, 121, 4121, 121, 1129),
    "setfsgid": (152, 139, 123, 1073741947, 139, 4139, 139, 1143),
    "setfsgid32": (-1, 216, -1, -1, 216, -1, -1, -1),
    "setfsuid": (151, 138, 122, 1073741946, 138, 4138, 138, 1142),
    "setfsuid32": (-1, 215, -1, -1, 215, -1, -1, -1),
    "setgid": (144, 46, 106, 1073741930, 46, 4046, 46, 1061),
    "setgid32": (-1, 214, -1, -1, 214, -1, -1, -1),
    "setgroups": (159, 81, 116, 1073741940, 81, 4081, 81, 1078),
    "setgroups32": (-1, 206, -1, -1, 206, -1, -1, -1),
    "sethostname": (161, 74, 170, 1073741994, 74, 4074, 74, 1083),
    "setitimer": (103, 104, 38, 1073741862, 104, 4104, 104, 1118),
    "setns": (268, 375, 308, 1073742132, 346, 4344, 350, 1330),
    "setpgid": (154, 57, 109, 1073741933, 57, 4057, 57, 1080),
    "setpriority": (140, 97, 141, 1073741965, 97, 4097, 97, 1102),
    "setregid": (143, 71, 114, 1073741938, 71, 4071, 71, 1072),
    "setregid32": (-1, 204, -1, -1, 204, -1, -1, -1),
    "setresgid": (149, 170, 119, 1073741943, 170, 4190, 169, 1076),
    "setresgid32": (-1, 210, -1, -1, 210, -1, -1, -1),
    "setresuid": (147, 164, 117, 1073741941, 164, 4185, 164, 1074),
    "setresuid32": (-1, 208, -1, -1, 208, -1, -1, -1),
    "setreuid": (145, 70, 113, 1073741937, 70, 4070, 70, 1071),
    "setreuid32": (-1, 203, -1, -1, 203, -1, -1, -1),
    "setrlimit": (164, 75, 160, 1073741984, 75, 4075, 75, 1084),
    "setsid": (157, 66, 112, 1073741936, 66, 4066, 66, 1081),
    "setsockopt": (208, 294, 54, 1073742365, 366, 4181, 339, 1203),
    "settimeofday": (170, 79, 164, 1073741988, 79, 4079, 79, 1088),
    "setuid": (146, 23, 105, 1073741929, 23, 4023, 23, 1045),
    "setuid32": (-1, 213, -1, -1, 213, -1, -1, -1),
    "setxattr": (5, 226, 188, 1073742012, 226, 4224, 209, 1217),
    "sgetmask": (-1, -1, -1, -1, 68, 4068, 68, -1),
    "shmat": (196, 305, 30, 1073741854, 397, 4397, 397, 1114),
    "shmctl": (195, 308, 31, 1073741855, 396, 4396, 396, 1116),
    "shmdt": (197, 306, 67, 1073741891, 398, 4398, 398, 1115),
    "shmget": (194, 307, 29, 1073741853, 395, 4395, 395, 1113),
    "shutdown": (210, 293, 48, 1073741872, 373, 4182, 338, 1202),
    "sigaction": (-1, 67, -1, -1, 67, 4067, 67, -1),
    "sigaltstack": (132, 186, 131, 1073742349, 186, 4206, 185, 1176),
    "signal": (-1, -1, -1, -1, 48, 4048, 48, -1),
    "signalfd": (-1, 349, 282, 1073742106, 321, 4317, 305, 1307),
    "signalfd4": (74, 355, 289, 1073742113, 327, 4324, 313, 1313),
    "sigpending": (-1, 73, -1, -1, 73, 4073, 73, -1),
    "sigprocmask": (-1, 126, -1, -1, 126, 4126, 126, -1),
    "sigreturn": (-1, 119, -1, -1, 119, 4119, 119, -1),
    "sigsuspend": (-1, 72, -1, -1, 72, 4072, 72, -1),
    "socket": (198, 281, 41, 1073741865, 359, 4183, 326, 1190),
    # modified socketcall arm -1 -> 102
    "socketcall": (-1, 102, -1, -1, 102, 4102, 102, -1),
    "socketpair": (199, 288, 53, 1073741877, 360, 4184, 333, 1197),
    "splice": (76, 340, 275, 1073742099, 313, 4304, 283, 1297),
    "spu_create": (-1, -1, -1, -1, -1, -1, 279, -1),
    "spu_run": (-1, -1, -1, -1, -1, -1, 278, -1),
    "ssetmask": (-1, -1, -1, -1, 69, 4069, 69, -1),
    "stat": (-1, 106, 4, 1073741828, 106, 4106, 106, 1210),
    "stat64": (-1, 195, -1, -1, 195, 4213, 195, -1),
    "statfs": (43, 99, 137, 1073741961, 99, 4099, 99, 1103),
    "statfs64": (-1, 266, -1, -1, 268, 4255, 252, 1258),
    "statx": (291, 397, 332, 1073742156, 383, 4366, 383, 1350),
    "stime": (-1, -1, -1, -1, 25, 4025, 25, -1),
    "stty": (-1, -1, -1, -1, 31, 4031, 31, -1),
    "subpage_prot": (-1, -1, -1, -1, -1, -1, 310, -1),
    "swapcontext": (-1, -1, -1, -1, -1, -1, 249, -1),
    "swapoff": (225, 115, 168, 1073741992, 115, 4115, 115, 1095),
    "swapon": (224, 87, 167, 1073741991, 87, 4087, 87, 1094),
    "switch_endian": (-1, -1, -1, -1, -1, -1, 363, -1),
    "symlink": (-1, 83, 88, 1073741912, 83, 4083, 83, 1091),
    "symlinkat": (36, 331, 266, 1073742090, 304, 4297, 295, 1290),
    "sync": (81, 36, 162, 1073741986, 36, 4036, 36, 1050),
    "sync_file_range": (84, -1, 277, 1073742101, 314, 4305, -1, 1300),
    "sync_file_range2": (-1, 341, -1, -1, -1, -1, 308, -1),
    "syncfs": (267, 373, 306, 1073742130, 344, 4342, 348, 1329),
    "sys_debug_setcontext": (-1, -1, -1, -1, -1, -1, 256, -1),
    # https://chromium.googlesource.com/native_client/nacl-newlib/+/master/libgloss/arm/linux-syscall.h
    # Found that sys_syscall is a thing
    "syscall": (-1, 113, -1, -1, -1, -1, -1, -1),
    "sysfs": (-1, 135, 139, 1073741963, 135, 4135, 135, 1139),
    "sysinfo": (179, 116, 99, 1073741923, 116, 4116, 116, 1127),
    "syslog": (116, 103, 103, 1073741927, 103, 4103, 103, 1117),
    "sysmips": (-1, -1, -1, -1, -1, 4149, -1, -1),
    "tee": (77, 342, 276, 1073742100, 315, 4306, 284, 1301),
    "tgkill": (131, 268, 234, 1073742058, 270, 4266, 250, 1235),
    # MODIFIED arm: 13
    "time": (-1, 13, 201, 1073742025, 13, 4013, 13, -1),
    "timer_create": (107, 257, 222, 1073742350, 259, 4257, 240, 1248),
    "timer_delete": (111, 261, 226, 1073742050, 263, 4261, 244, 1252),
    "timer_getoverrun": (109, 260, 225, 1073742049, 262, 4260, 243, 1251),
    "timer_gettime": (108, 259, 224, 1073742048, 261, 4259, 242, 1250),
    "timer_gettime64": (-1, 408, -1, -1, 408, 4408, 408, -1),
    "timer_settime": (110, 258, 223, 1073742047, 260, 4258, 241, 1249),
    "timer_settime64": (-1, 409, -1, -1, 409, 4409, 409, -1),
    "timerfd": (-1, -1, -1, -1, -1, 4318, -1, 1308),
    "timerfd_create": (85, 350, 283, 1073742107, 322, 4321, 306, 1310),
    "timerfd_gettime": (87, 354, 287, 1073742111, 326, 4322, 312, 1312),
    "timerfd_gettime64": (-1, 410, -1, -1, 410, 4410, 410, -1),
    "timerfd_settime": (86, 353, 286, 1073742110, 325, 4323, 311, 1311),
    "timerfd_settime64": (-1, 411, -1, -1, 411, 4411, 411, -1),
    "times": (153, 43, 100, 1073741924, 43, 4043, 43, 1059),
    "tkill": (130, 238, 200, 1073742024, 238, 4236, 208, 1229),
    "truncate": (45, 92, 76, 1073741900, 92, 4092, 92, 1097),
    "truncate64": (-1, 193, -1, -1, 193, 4211, 193, -1),
    "tuxcall": (-1, -1, 184, 1073742008, -1, -1, 225, -1),
    "ugetrlimit": (-1, 191, -1, -1, 191, -1, 190, -1),
    "ulimit": (-1, -1, -1, -1, 58, 4058, 58, -1),
    "umask": (166, 60, 95, 1073741919, 60, 4060, 60, 1067),
    "umount": (-1, -1, -1, -1, 22, 4022, 22, 1044),
    "umount2": (39, 52, 166, 1073741990, 52, 4052, 52, 1044),
    "uname": (160, 122, 63, 1073741887, 122, 4122, 122, 1130),
    "unlink": (-1, 10, 87, 1073741911, 10, 4010, 10, 1032),
    "unlinkat": (35, 328, 263, 1073742087, 301, 4294, 292, 1287),
    "unshare": (97, 337, 272, 1073742096, 310, 4303, 282, 1296),
    "uselib": (-1, 86, 134, -1, 86, 4086, 86, 1093),
    "userfaultfd": (282, 388, 323, 1073742147, 374, 4357, 364, 1343),
    "ustat": (-1, 62, 136, 1073741960, 62, 4062, 62, 1069),
    "utime": (-1, -1, 132, 1073741956, 30, 4030, 30, -1),
    "utimensat": (88, 348, 280, 1073742104, 320, 4316, 304, 1306),
    "utimensat_time64": (-1, 412, -1, -1, 412, 4412, 412, -1),
    "utimes": (-1, 269, 235, 1073742059, 271, 4267, 251, 1036),
    "vfork": (-1, 190, 58, 1073741882, 190, -1, 189, -1),
    "vhangup": (58, 111, 153, 1073741977, 111, 4111, 111, 1123),
    "vm86": (-1, -1, -1, -1, 166, 4113, 113, -1),
    "vm86old": (-1, -1, -1, -1, 113, -1, -1, -1),
    "vmsplice": (75, 343, 278, 1073742356, 316, 4307, 285, 1302),
    "vserver": (-1, 313, 236, -1, 273, 4277, -1, 1269),
    "wait4": (260, 114, 61, 1073741885, 114, 4114, 114, 1126),
    "waitid": (95, 280, 247, 1073742353, 284, 4278, 272, 1270),
    "waitpid": (-1, -1, -1, -1, 7, 4007, 7, -1),
    "write": (64, 4, 1, 1073741825, 4, 4004, 4, 1027),
    "writev": (66, 146, 20, 1073742340, 146, 4146, 146, 1147),
}