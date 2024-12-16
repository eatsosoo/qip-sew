# constants.py
# -*- coding: utf-8 -*-
# Table headers
HORIZONTAL_HEADERS = [
    "07:30-08:30", 
    "08:30-09:30", 
    "09:30-10:30", 
    "10:30-11:30", 
    "11:30-12:30",
    "12:30-13:30",
    "13:30-14:30", 
    "14:30-15:30", 
    "15:30-16:30", 
    "16:30-17:30", 
    "17:30-18:30", 
    "18:30-19:30"
]

VERTICAL_HEADERS = [
    u"Số hàng cần kiểm", 
    u"Số hàng lỗi", 
    u"Tỉ lệ lỗi (%)"
]

COLUMNS = {
    "DTQC1001": u"May hợp không thẳng",
    "DTQC1002": u"Dán lót hậu xấu",
    "DTQC1003": u"Lót ngắn, lót nhăn",
    "DTQC1004": u"Định hình mũ bị nhăn",
    "DTQC1005": u"Xía miên nhăn",
    "DTQC1006": u"May khóa bị lệch",
    "DTQC1007": u"Cắt mí nây nỷ không đẹp",
    "DTQC1008": u"Đồ sơn xấu",
    "DTQC1009": u"Nây nỷ sai tem",
    "DTQC1010": u"Khoảng cách mí không đều",
    "DTQC1011": u"Cổ giày và miệng giày cao thấp",
    "DTQC1012": u"Logo cao thấp",
    "DTQC1013": u"Đầu chỉ",
    "DTQC1014": u"Khoảng cách may không đều",
    "DTQC1015": u"May ziczac xấu",
    "DTQC1016": u"Xía miên khác màu",
    "DTQC1017": u"Mũ giày bẩn",
    "DTQC1018": u"Sai chỉ",
    "DTQC1019": u"May không đúng vị trí",
    # "DRQC1001": u"May hợp không thẳng",
    # "DRQC1002": u"Dán lót hậu xấu",
    # "DRQC1003": u"Lót ngắn, lót nhăn",
    # "DRQC1004": u"Định hình mũ bị nhăn",
    # "DRQC1005": u"Xía miên nhăn",
    # "DRQC1006": u"May khóa bị lệch",
    # "DRQC1007": u"Cắt mí nây nỷ không đẹp",
    # "DRQC1008": u"Đồ sơn xấu",
    # "DRQC1009": u"Nây nỷ sai tem",
    # "DRQC1010": u"Khoảng cách mí không đều",
    # "DRQC1011": u"Cổ giày và miệng giày cao thấp",
    # "DRQC1012": u"Logo cao thấp",
    # "DRQC1013": u"Đầu chỉ",
    # "DRQC1014": u"Khoảng cách may không đều",
    # "DRQC1015": u"May ziczac xấu",
    # "DRQC1016": u"Xía miên khác màu",
    # "DRQC1017": u"Vệ sinh bẩn, xía miên không sạch",
    # "DRQC1018": u"Sai chỉ",
    # "DRQC1019": u"May không đúng vị trí",
    # "DRQC1020": u"Xía miên bị cong, nghiêng",
    # "DRQC1021": u"Kim bị lỗi",
    # "DRQC1022": u"Lỗ đục ở lưỡi gà xấu",
    # "DRQC1023": u"May thiếu",
    # "DRQC1024": u"Sai vị trí tăng cường",
}

SEW_ERRORS = {
    "combination_is_marked": u"Tổ hợp bị hằn",
    "combination_has_open_grinding": u"Tổ hợp bị hở bào mài",
    "unfavorable_sewing_line": u"Đường gò không thuận",
    "sewing_thread_error": u"Đường may chỉ lỗi",
    "back_height_uneven_misaligned": u"Hậu cao thấp, lệch hậu",
    "nay_niry_too_high_unfavorable": u"Nây nỷ nhô cao, không thuận",
    "hair_length_uneven_not_yet_shed": u"Lông dài ngắn, chưa gảy lông",
    "button_is_loose_tight_reversed_missing": u"Khuy Oze lỏng, chặt, ngược, thiếu",
    "edge_is_dented_wrinkled_uneven_length": u"Viền móp, nhăn, dài ngắn",
    "stitching_is_missing_loose_tight": u"Khâu thiếu, lỏng, chặt",
    "fabric_color_faded_hair_cracked": u"Xía miên mất màu, rạn nứt lông",
    "zipper_head_uneven_height": u"Đầu khóa, la len cao thấp",
    "shape_line_not_enough_curvature": u"Vệt định hình, không đủ độ cong",
    "elastic_thread_not_straight": u"Chun rút sợi không thẳng",
    "raw_cow_head_uneven_high_low": u"Đầu bò sống lệch, cao thấp",
    "ear_strap_uneven_short_long": u"Dây tai dài ngắn, lệch",
    "hole_punched_torn_misaligned_not_clear": u"Đục lỗ toét, lệch, không thông",
    "valid_combination_not_flexible": u"Hợp lệch xía uyển",
    "fake_stitching_pencil_line_on_form": u"May giả chỉ, vạch chì chân phom",
    "back_shaping_knife_insertion_incorrect": u"Định hình hậu xỏ dao không đúng",
}

SEW_GL3 = {
    "bonding_gap_on_attached_line": u"Hở keo đường tỏ hợp chết",
    "frayed_edge": u"Tưa sợi",
    "broken_elastic": u"Bục chun",
    "iconsistent_elastic_length": u"Chun dài ngắn",
    "run_off_stitching_on_lining_margin": u"May trượt mí lót",
    "poor_mudguard_attaching": u"Tổ hợp trang trí không tiêu chuẩn",
    "inconsistent_eyelet_attaching": u"Tổ hợp mắt giày cao thấp",
    "broken_collar": u"Bục cổ giày",
    "wheel_mark": u"Hằn bánh xe",
    "roller_mark": u"Lỗ chân kim",
    "wrinkles_collar_foam": u"Nhăn cổ phao",
}

PRIMARY_COLOR = '#00c04b'
DANGER_COLOR = '#ff5b00'

STYLE_SCROLLBAR = """
    QScrollBar:vertical {
        border: none;
        background: #f5f5f5;  /* Màu nền */
        width: 8px;  /* Độ rộng thanh cuộn dọc */
        margin: 0px 0px 0px 0px;
    }

    QScrollBar::handle:vertical {
        background: #c4c4c4;  /* Màu thanh cuộn */
        min-height: 20px;
        border-radius: 4px;  /* Bo góc */
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        border: none;
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        border: none;
        background: #f5f5f5;  /* Màu nền */
        height: 8px;  /* Độ cao thanh cuộn ngang */
        margin: 0px 0px 0px 0px;
    }

    QScrollBar::handle:horizontal {
        background: #c4c4c4;  /* Màu thanh cuộn */
        min-width: 20px;
        border-radius: 4px;  /* Bo góc */
    }

    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        border: none;
        background: none;
    }

    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }
"""