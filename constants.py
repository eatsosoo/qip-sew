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
    "Số hàng cần kiểm", 
    "Số hàng lỗi", 
    "Tỉ lệ lỗi (%)"
]

COLUMNS = {
    "DTQC1001": "May hợp không thẳng",
    "DTQC1002": "Dán lót hậu xấu",
    "DTQC1003": "Lót ngắn, lót nhăn",
    "DTQC1004": "Định hình mũ bị nhăn",
    "DTQC1005": "Xía miên nhăn",
    "DTQC1006": "May khóa bị lệch",
    "DTQC1007": "Cắt mí nây nỷ không đẹp",
    "DTQC1008": "Đồ sơn xấu",
    "DTQC1009": "Nây nỷ sai tem",
    "DTQC1010": "Khoảng cách mí không đều",
    "DTQC1011": "Cổ giày và miệng giày cao thấp",
    "DTQC1012": "Logo cao thấp",
    "DTQC1013": "Đầu chỉ",
    "DTQC1014": "Khoảng cách may không đều",
    "DTQC1015": "May ziczac xấu",
    "DTQC1016": "Xía miên khác màu",
    "DTQC1017": "Mũ giày bẩn",
    "DTQC1018": "Sai chỉ",
    "DTQC1019": "May không đúng vị trí",
    # "DRQC1001": "May hợp không thẳng",
    # "DRQC1002": "Dán lót hậu xấu",
    # "DRQC1003": "Lót ngắn, lót nhăn",
    # "DRQC1004": "Định hình mũ bị nhăn",
    # "DRQC1005": "Xía miên nhăn",
    # "DRQC1006": "May khóa bị lệch",
    # "DRQC1007": "Cắt mí nây nỷ không đẹp",
    # "DRQC1008": "Đồ sơn xấu",
    # "DRQC1009": "Nây nỷ sai tem",
    # "DRQC1010": "Khoảng cách mí không đều",
    # "DRQC1011": "Cổ giày và miệng giày cao thấp",
    # "DRQC1012": "Logo cao thấp",
    # "DRQC1013": "Đầu chỉ",
    # "DRQC1014": "Khoảng cách may không đều",
    # "DRQC1015": "May ziczac xấu",
    # "DRQC1016": "Xía miên khác màu",
    # "DRQC1017": "Vệ sinh bẩn, xía miên không sạch",
    # "DRQC1018": "Sai chỉ",
    # "DRQC1019": "May không đúng vị trí",
    # "DRQC1020": "Xía miên bị cong, nghiêng",
    # "DRQC1021": "Kim bị lỗi",
    # "DRQC1022": "Lỗ đục ở lưỡi gà xấu",
    # "DRQC1023": "May thiếu",
    # "DRQC1024": "Sai vị trí tăng cường",
}

SEW_ERRORS = {
    "combination_is_marked": "Tổ hợp bị hằn",
    "combination_has_open_grinding": "Tổ hợp bị hở bào mài",
    "unfavorable_sewing_line": "Đường gò không thuận",
    "sewing_thread_error": "Đường may chỉ lỗi",
    "back_height_uneven_misaligned": "Hậu cao thấp, lệch hậu",
    "nay_niry_too_high_unfavorable": "Nây nỷ nhô cao, không thuận",
    "hair_length_uneven_not_yet_shed": "Lông dài ngắn, chưa gảy lông",
    "button_is_loose_tight_reversed_missing": "Khuy Oze lỏng, chặt, ngược, thiếu",
    "edge_is_dented_wrinkled_uneven_length": "Viền móp, nhăn, dài ngắn",
    "stitching_is_missing_loose_tight": "Khâu thiếu, lỏng, chặt",
    "fabric_color_faded_hair_cracked": "Xía miên mất màu, rạn nứt lông",
    "zipper_head_uneven_height": "Đầu khóa, la len cao thấp",
    "shape_line_not_enough_curvature": "Vệt định hình, không đủ độ cong",
    "elastic_thread_not_straight": "Chun rút sợi không thẳng",
    "raw_cow_head_uneven_high_low": "Đầu bò sống lệch, cao thấp",
    "ear_strap_uneven_short_long": "Dây tai dài ngắn, lệch",
    "hole_punched_torn_misaligned_not_clear": "Đục lỗ toét, lệch, không thông",
    "valid_combination_not_flexible": "Hợp lệch xía uyển",
    "fake_stitching_pencil_line_on_form": "May giả chỉ, vạch chì chân phom",
    "back_shaping_knife_insertion_incorrect": "Định hình hậu xỏ dao không đúng",
}

SEW_GL3 = {
    "bonding_gap_on_attached_line": "Hở keo đường tỏ hợp chết",
    "frayed_edge": "Tưa sợi",
    "broken_elastic": "Bục chun",
    "iconsistent_elastic_length": "Chun dài ngắn",
    "run_off_stitching_on_lining_margin": "May trượt mí lót",
    "poor_mudguard_attaching": "Tổ hợp trang trí không tiêu chuẩn",
    "inconsistent_eyelet_attaching": "Tổ hợp mắt giày cao thấp",
    "broken_collar": "Bục cổ giày",
    "wheel_mark": "Hằn bánh xe",
    "roller_mark": "Lỗ chân kim",
    "wrinkles_collar_foam": "Nhăn cổ phao",
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