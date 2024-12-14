# constants.py

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