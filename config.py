# Choose the file from which you want to collect data offline
file_name = "Data\F.csv"
cal_file_name = "Data\F-Cal.csv"

#========================================================#

# Select IMU IDs and body parts from here #
id_to_body = {
            2: 'pelvis_imu',
            12: 'hand_r_imu',
             }

IDs = list(id_to_body.keys())

# Choose id_to_body from the below list #
'''
    "hand_r_imu",    // دست راست
    "hand_l_imu",    // دست چپ
    "radius_r_imu",  // ساعد راست
    "radius_l_imu",  // ساعد چپ
    "humerus_r_imu", // بازو راست
    "humerus_l_imu", // بازو چپ
    "torso_imu",     // سینه/تنه
    "pelvis_imu",    // پشت
    "femur_r_imu",   // ران راست
    "femur_l_imu",   // ران چپ
    "tibia_r_imu",   // ساق راست
    "tibia_l_imu",   // ساق چپ
    "calcn_r_imu",   // پاشنه راست
    "calcn_l_imu",   // پاشنه چپ
'''
#========================================================#

# Choose the joints you want to save #

joint_name = [
'pelvis_tilt',         # شیب لگن
'pelvis_list',         # کج‌شدن جانبی لگن
'pelvis_rotation',     # چرخش لگن
# 'pelvis_tx',           # جابه‌جایی لگن در محور x
# 'pelvis_ty',           # جابه‌جایی لگن در محور y
# 'pelvis_tz',           # جابه‌جایی لگن در محور z
'arm_flex_r',          # خم شدن بازوی راست
'arm_add_r',           # نزدیک شدن بازوی راست
'arm_rot_r',           # چرخش بازوی راست
'elbow_flex_r',        # خم شدن آرنج راست
# 'lumbar_extension',    # بسط ستون فقرات
# 'lumbar_bending',      # خم شدن ستون فقرات
# 'lumbar_rotation',     # چرخش ستون فقرات
# 'hip_flexion_r',       # خم شدن ران راست
# 'hip_adduction_r',     # نزدیک شدن ران راست
# 'hip_rotation_r',      # چرخش ران راست
# 'knee_angle_r',        # زاویه زانوی راست
# 'knee_angle_r_beta',   # زاویه بتای زانوی راست
# 'ankle_angle_r',       # زاویه مچ پای راست
# 'subtalar_angle_r',    # زاویه قوزک پای راست
# 'mtp_angle_r',         # زاویه مفصل انگشتان پای راست
# 'hip_flexion_l',       # خم شدن ران چپ
# 'hip_adduction_l',     # نزدیک شدن ران چپ
# 'hip_rotation_l',      # چرخش ران چپ
# 'knee_angle_l',        # زاویه زانوی چپ
# 'knee_angle_l_beta',   # زاویه بتای زانوی چپ
# 'ankle_angle_l',       # زاویه مچ پای چپ
# 'subtalar_angle_l',    # زاویه قوزک پای چپ
# 'mtp_angle_l',         # زاویه مفصل انگشتان پای چپ
# 'wrist_flex_r',        # خم شدن مچ راست
# 'wrist_dev_r',         # انحراف مچ راست
# 'arm_flex_l',          # خم شدن بازوی چپ
# 'arm_add_l',           # نزدیک شدن بازوی چپ
# 'arm_rot_l',           # چرخش بازوی چپ
# 'elbow_flex_l',        # خم شدن آرنج چپ
# 'wrist_flex_l',        # خم شدن مچ چپ
# 'wrist_dev_l'          # انحراف مچ چپ
# 'pro_sup_r',           # برگشت کف دست راست (به بالا/پایین)
# 'pro_sup_l',           # برگشت کف دست چپ (به بالا/پایین)
 ]