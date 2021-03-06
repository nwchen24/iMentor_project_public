##/usr/bin/python3

# Program to create master_table and load from csv 

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS master_table
	(mentee_user_id INT,
	most_recent_mentor_persona_id INT,
	most_recent_mentor_user_id INT,
	admin_id INT,
	parent INT,
	member_id INT,
	school INT,
	grad_yr INT,
	prog_type INT,
	highschool_or_college INT,
	yop INT,
	num_mentors_per_mentee INT,
	first_yr_flag INT,
	oop_status INT,
	match_start_date DATE,
	match_end_date DATE,
	lom INT,
	mentee_gender INT,
	mentee_eth INT,
	mentee_nonwhite INT,
	mentee_frl INT,
	mentee_fgen INT,
	mentor_eth INT,
	mentor_fgen INT,
	mentee_active_boy_1213 INT,
	mentee_active_boy_1314 INT,
	mentee_active_boy_1415 INT,
	mentee_active_boy_1516 INT,
	mentee_active_eoy_1213 INT,
	mentee_active_eoy_1314 INT,
	mentee_active_eoy_1415 INT,
	mentee_active_eoy_1516 INT,
	mentor_active_boy_1213 INT,
	mentor_active_boy_1314 INT,
	mentor_active_boy_1415 INT,
	mentor_active_boy_1516 INT,
	mentor_active_eoy_1213 INT,
	mentor_active_eoy_1314 INT,
	mentor_active_eoy_1415 INT, 
	mentor_active_eoy_1516 INT,
	mentee_tp_1314 INT,
	mentee_tp_1415 INT,
	mentee_tp_1415_bm INT,
	mentee_tp_1415_c INT,
	mentee_tp_1516 INT,
	mentee_tp_1516_bm INT,
	mentee_tp_1516_c INT,
	mentor_tp_1314 INT,
	mentor_tp_1415 INT,
	mentor_tp_1415_bm INT,
	mentor_tp_1415_c INT,
	mentor_tp_1516 INT,
	mentor_tp_1516_bm INT,
	mentor_tp_1516_c INT,
	f12ssc_score FLOAT,
	s13ssc_score FLOAT,
	f12prs_score FLOAT,
	s13prs_score FLOAT,
	f12loc_score FLOAT,
	s13loc_score FLOAT,
	f12tap_score FLOAT,
	s13tap_score FLOAT,
	f12hop_score FLOAT,
	s13hop_score FLOAT,
	f12hsa_score FLOAT,
	f12edugoal FLOAT,
	s13edugoal FLOAT,
	f12eduexp FLOAT,
	s13eduexp FLOAT,
	f12edumin FLOAT,
	s13edumin FLOAT,
	f12cas3 FLOAT,
	s13cas3 FLOAT,
	mentee_online_freq_1213  FLOAT,
	mentor_online_freq_1213  FLOAT,
	pair_online_freq_1213  FLOAT,
	pair_meetings_1213  FLOAT,
	lesson_benchmark_50_1213 FLOAT,
	lesson_benchmark_55_1213 FLOAT,
	lesson_benchmark_60_1213 FLOAT,
	lesson_benchmark_65_1213 FLOAT,
	lesson_benchmark_70_1213 FLOAT,
	lesson_benchmark_75_1213 FLOAT,
	inperson_benchmark_4_1213 FLOAT,
	inperson_benchmark_5_1213 FLOAT,
	inperson_benchmark_6_1213 FLOAT,
	inperson_benchmark_7_1213 FLOAT,
	f13loc_score FLOAT,
	s14loc_score FLOAT,
	f13ssc_score FLOAT, 
	s14ssc_score FLOAT,
	f13cul_score FLOAT,
	s14cul_score FLOAT,
	f13cll_score FLOAT,
	s14cll_score FLOAT,
	f13hop_score FLOAT,
	s14hop_score FLOAT,
	f13prs_score FLOAT,
	s14prs_score FLOAT,
	f13imp_score FLOAT,
	s14imp_score FLOAT,
	f13tap_score FLOAT,
	s14tap_score FLOAT,
	f13spr_score FLOAT,
	s14spr_score FLOAT,
	f13edugoal FLOAT,
	s14edugoal FLOAT,
	f13eduexp FLOAT,
	s14eduexp FLOAT,
	f13edumin FLOAT,
	s14edumin FLOAT,
	f13cas3 FLOAT,
	s14cas3 FLOAT,
	pair_online_freq_1314_A FLOAT,
	pair_meetings_1314_A FLOAT,
	lesson_benchmark_50_1314_A FLOAT,
	lesson_benchmark_55_1314_A FLOAT,
	lesson_benchmark_60_1314_A FLOAT,
	lesson_benchmark_65_1314_A FLOAT,
	lesson_benchmark_70_1314_A FLOAT,
	lesson_benchmark_75_1314_A FLOAT,
	inperson_benchmark_4_1314_A FLOAT,
	inperson_benchmark_5_1314_A FLOAT,
	inperson_benchmark_6_1314_A FLOAT,
	inperson_benchmark_7_1314_A FLOAT,
	f14spr_score FLOAT,
	s15spr_score FLOAT,
	f14mya9 FLOAT,
	s15mya9 FLOAT,
	f14tap_score FLOAT,
	s15tap_score FLOAT,
	f14loc_score  FLOAT,
	s15loc_score  FLOAT,
	f14prs_score  FLOAT,
	s15prs_score  FLOAT,
	f14hop_score  FLOAT,
	s15hop_score  FLOAT,
	f14cll_score  FLOAT,
	s15cll_score  FLOAT,
	f14ssc_score  FLOAT,
	s15ssc_score  FLOAT,
	f14imp_score  FLOAT,
	s15imp_score  FLOAT,
	f14hlp_score  FLOAT,
	s15hlp_score  FLOAT,
	s15edugoal  FLOAT,
	s15eduexp  FLOAT,
	s15edumin  FLOAT,
	s15cas3 FLOAT,
	s15edugoal_d FLOAT,
	s15eduexp_d FLOAT,
	s15edumin_d FLOAT,
	trst_att_1 FLOAT,
	trst_att_2 FLOAT,
	trst_att_3 FLOAT,
	mentee_online_freq_1415 FLOAT,
	mentor_online_freq_1415 FLOAT,
	pair_online_freq_1415 FLOAT,
	pair_total_mtgs_1415 FLOAT,
	lesson_benchmark_50_1415 FLOAT,
	lesson_benchmark_55_1415 FLOAT,
	lesson_benchmark_60_1415 FLOAT,
	lesson_benchmark_65_1415 FLOAT,
	lesson_benchmark_70_1415 FLOAT,
	lesson_benchmark_75_1415 FLOAT,
	inperson_benchmark_4_1415 FLOAT,
	inperson_benchmark_5_1415 FLOAT,
	inperson_benchmark_6_1415 FLOAT,
	inperson_benchmark_7_1415 FLOAT,
	eoy_psr_rowsum_1415 FLOAT,
	eoy_psr_manage_focus_list_1415 FLOAT,
	eoy_psr_reactive_pair_support_1415 FLOAT,
	eoy_psr_coaching_healthy_rel_1415 FLOAT,
	eoy_psr_info_utilization_1415 FLOAT,
	my_mr_score_1415 FLOAT,
	eoy_mr_score_1415 FLOAT,
	mr_score_avg_1415 FLOAT,
	mentee_online_freq_1516 FLOAT,
	mentor_online_freq_1516 FLOAT,
	pair_online_freq_1516 FLOAT,
	pair_curriculum_mtgs_1516 FLOAT,
	pair_other_mtgs_1516 FLOAT,
	pair_oop_mtgs_1516 FLOAT,
	pair_total_mtgs_1516 FLOAT,
	mentee_conversation_cnt_1516 FLOAT,
	mentor_conversation_cnt_1516 FLOAT,
	pair_conversation_cnt_1516 FLOAT,
	lesson_benchmark_50_1516 FLOAT,
	lesson_benchmark_55_1516 FLOAT,
	lesson_benchmark_60_1516 FLOAT,
	lesson_benchmark_65_1516 FLOAT,
	lesson_benchmark_70_1516 FLOAT,
	lesson_benchmark_75_1516 FLOAT,
	inperson_benchmark_4_1516 FLOAT,
	inperson_benchmark_5_1516 FLOAT,
	inperson_benchmark_6_1516 FLOAT,
	inperson_benchmark_7_1516 FLOAT,
	inperson_benchmark_8 FLOAT,
	f15spr_score_mentee FLOAT,
	s16mya_sumscore FLOAT,
	s16spr_meanscore FLOAT,
	f15spr_score_mentor FLOAT,
	f15ssc_score FLOAT,
	s16ssc_score FLOAT,
	f15loc_score FLOAT,
	s16loc_score FLOAT,
	f15tap_score FLOAT,
	s16tap_score FLOAT,
	f15prs_score FLOAT,
	s16prs_score FLOAT,
	f15hlp_score FLOAT,
	s16hlp_score FLOAT,
	f15hop_score FLOAT,
	s16hop_score FLOAT,
	f15lotr_mean FLOAT,
	f15lotr_score FLOAT,
	s16lotr_score FLOAT,
	s16imp_score FLOAT,
	f15ggf5 FLOAT,
	s16ggf5 FLOAT,
	f15ggf5_d FLOAT,
	f15mya10 FLOAT,
	f15mya10_d FLOAT,
	s16mya10 FLOAT,
	f15mya2 FLOAT,
	f15mya2_d FLOAT,
	s16mya2 FLOAT,
	f15mya3 FLOAT,
	f15mya3_d FLOAT,
	s16mya3 FLOAT,
	f15mya4 FLOAT,
	f15mya4_d FLOAT,
	s16mya4 FLOAT,
	s16mya4_d FLOAT,
	f15mya5 FLOAT,
	f15mya5_d FLOAT,
	s16mya5 FLOAT,
	s16mya5_d FLOAT,
	f15mya6 FLOAT,
	f15mya6_d FLOAT,
	s16mya6 FLOAT,
	f15mya7 FLOAT,
	f15mya7_d FLOAT,
	s16mya7 FLOAT,
	f15mya9 FLOAT,
	f15mya9_d FLOAT,
	s16mya9 FLOAT,
	s16mya9_d FLOAT,
	f15edugoal FLOAT,
	f15eduexp FLOAT,
	f15edumin FLOAT,
	s16edugoal FLOAT,
	s16eduexp FLOAT,
	s16edumin FLOAT,
	f15edugoal_d FLOAT,
	s16edugoal_d FLOAT,
	f15eduexp_d FLOAT,
	s16eduexp_d FLOAT,
	f15edumin_d FLOAT,
	s16edumin_d FLOAT,
	f15cas3 FLOAT,
	s16cas3 FLOAT,
	f15mentor_mya2 FLOAT,
	f15mentor_mya2_d FLOAT,
	s16mentor_mya2 FLOAT,
	f15mentor_mya3 FLOAT,
	f15mentor_mya3_d FLOAT,
	s16mya3_mentor FLOAT,
	f15mentor_mya4 FLOAT,
	f15mentor_mya4_d FLOAT,
	s16mya4_mentor FLOAT,
	f15mentor_mya5 FLOAT,
	f15mentor_mya5_d FLOAT,
	s16mya5_mentor FLOAT,
	f15mentor_mya1 FLOAT,
	f15mentor_mya1_d FLOAT,
	s16mentor_mya_1 FLOAT,
	f15mentor_mya7 FLOAT,
	f15mentor_mya7_d FLOAT,
	s16mya7_mentor FLOAT,
	f15mentor_mya9 FLOAT,
	f15mentor_mya9_d FLOAT,
	s16mya9_mentor FLOAT,
	s16mya10_mentor FLOAT,
	s16mya13_mentor FLOAT,
	s16aftschenr1 FLOAT,
	s16aftschenr2 FLOAT,
	s16aftschjob1 FLOAT,
	s16aftschjob2 FLOAT,
	s16sumenrich1 FLOAT,
	s16sumenrich3 FLOAT,
	s16goal1 FLOAT,
	s16goal2 FLOAT,
	s16pro12 FLOAT,
	s16pro13 FLOAT,
	s16pro15 FLOAT,
	s16pro16 FLOAT,
	s16pro17 FLOAT,
	s16pro18 FLOAT,
	s16pro14 FLOAT,
	s16pro14_c FLOAT,
	s16pro13_c FLOAT,
	s16pro18_c FLOAT,
	s16mentorcom1 FLOAT,
	s16mentorcom2 FLOAT,
	s16mentorcom3 FLOAT,
	s16mentorcom5 FLOAT,
	s16pe8 FLOAT,
	s16pe12 FLOAT,
	s16cm_rrm FLOAT,
	s16cm_goal1 FLOAT,
	s16cm_goal2 FLOAT,
	s16me_enrsch1 FLOAT,
	s16me_enrsum1 FLOAT,
	s16comm_phn_fr FLOAT,
	s16comm_sms_fr FLOAT,
	s16comm_email FLOAT,
	mr_consistent_mtg_1516 FLOAT,
	mr_consistent_online_1516 FLOAT,
	mr_strengths_based_1516 FLOAT,
	mr_util_resources_1516 FLOAT,
	mr_responsive_1516 FLOAT,
	mr_model_curric_1516 FLOAT,
	mr_score_1516 FLOAT,
	f15_to_s16_spr_change FLOAT,
	f15_to_s16_loc_change FLOAT,
	f15_to_s16_tap_change FLOAT,
	f15_to_s16_prs_change FLOAT,
	f15_to_s16_hlp_change FLOAT,
	f15_to_s16_hop_change FLOAT,
	f15_to_s16_lotr_change FLOAT,
	f15_to_s16_ssc_change FLOAT,
	f14_to_s16_spr_change FLOAT,
	f14_to_s16_loc_change FLOAT,
	f14_to_s16_tap_change FLOAT,
	f14_to_s16_prs_change FLOAT,
	f14_to_s16_hlp_change FLOAT,
	f14_to_s16_hop_change FLOAT,
	f14_to_s16_ssc_change FLOAT,
	f13_to_s16_spr_change FLOAT,
	f13_to_s16_loc_change FLOAT,
	f13_to_s16_tap_change FLOAT,
	f13_to_s16_prs_change FLOAT,
	f13_to_s16_hop_change FLOAT,
	f13_to_s16_ssc_change FLOAT,
	f12_to_s16_loc_change FLOAT,
	f12_to_s16_tap_change FLOAT,
	f12_to_s16_prs_change FLOAT,
	f12_to_s16_hop_change FLOAT,
	f12_to_s16_ssc_change FLOAT,
	ps_rubric_compelling_focus_list_1516 FLOAT,
	ps_rubric_documents_1516 FLOAT,
	ps_rubric_follow_up_1516 FLOAT,
	ps_rubric_responsivetomentors_1516 FLOAT,
	ps_rubric_escalation_1516 FLOAT,
	ps_rubric_challengingtopics_1516 FLOAT,
	ps_rubric_strengthsbasedmentees_1516 FLOAT,
	ps_rubric_strengthsbasedmentors_1516 FLOAT,
	ps_rubric_curriculum_1516 FLOAT,
	ps_rubric_schoolinfo_1516 FLOAT,
	ps_rubric_matchhistory_1516 FLOAT,
	ps_rubric_canvas_1516 FLOAT,
	ps_rubric_support_1516 FLOAT,
	ps_sum_score_1516 FLOAT,
	mr_score_sans_engage_var FLOAT,
	mr_score_sans_engage_d FLOAT,
	psr_rollup_score_focuslist FLOAT,
	psr_rollup_score_reactive FLOAT,
	psr_rollup_score_coaching FLOAT,
	psr_rollup_score_info_util FLOAT,
	filter_$ INT);''')
conn.commit()
	
sqlstr = "COPY master_table FROM STDIN DELIMITER ',' CSV"
with open('/home/levi/MIDS/Project/Table_6_master_eoy.csv') as f:
    cur.copy_expert(sqlstr, f)
conn.commit()


