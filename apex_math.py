from __future__ import division
import os

pak_level = 199
pak_bp_s1 = 11
pak_bp_s2 = 12
pak_bp_s3 = 12
pak_bp_s4 = 12
pak_bp_s5 = 12
pak_bp_s6 = 13
pak_bp_s7 = 15
pak_quest_s5 = 6
pak_quest_s6 = 7
pak_quest_s7 = 8
xp_per_sec = 3
xp_per_kill = 50
xp_per_dmg_point = 0.25
number_of_heirlooms = 7
average_game_time_full = float((18+21)/2) * 60
average_game_time_half = float((10+12)/2) * 60
tier_up_half_game = 54000/1300
tier_up_full_game = 54000/3000
total = pak_bp_s1 + pak_bp_s2 + pak_level + pak_bp_s3 + pak_bp_s4 + pak_quest_s5 + pak_quest_s6 + pak_bp_s5 + pak_bp_s6 + pak_quest_s7 + pak_bp_s7
chance = float((total/500) * 100)
wriath_heirloom_chance = float((1/number_of_heirlooms) * 100)
bloodhound_heirloom_chance = float((1/number_of_heirlooms) * 100)
lifeline_heirloom_chance = float((1/number_of_heirlooms) * 100)
pathfinder_heirloom_chance = float((1/number_of_heirlooms) * 100)
octane_heirloom_chance = float((1/number_of_heirlooms) * 100)
mirage_heirloom_chance = float((1/number_of_heirlooms) * 100)
caustic_heirloom_chance = float((1/number_of_heirlooms) * 100)

print("Heirloom Chance:")
print("Next pack opened is Heirloom: " + str(chance) + "%")
print("Next pack will NOT be a Heirloom: " + str(100 - chance) + "%")
print("*assuming you finished all 7 battlepasses,are level 500,finished all 3 quests and you did not buy any other packs")
print(" ")
print("Chance that Heirloom will be:")
print("Wriath's Kunai Knife: "+ str(wriath_heirloom_chance) + "%")
print("Bloodhound's Raven's Bite Axe: "+ str(bloodhound_heirloom_chance) + "%")
print("Lifeline's Shock Sticks Drumsticks: "+ str(lifeline_heirloom_chance) + "%")
print("Pathfinder's Boxing Gloves: "+ str(pathfinder_heirloom_chance) + "%")
print("Octane's Butterfly Knife: "+ str(octane_heirloom_chance) + "%")
print("Mirage's Too Much Witt Statue: " + str(mirage_heirloom_chance) + "%")
print("Caustic's Death Hammer: " + str(caustic_heirloom_chance) + "%")
print(" ")
print("XP earned:")
print("Full game surival time XP earned(Top 3): "+ str(average_game_time_full * xp_per_sec) + " XP")
print("Half game surival time XP earned(Top 10): "+ str(average_game_time_half * xp_per_sec) + " XP")
print(" ")
print("XP earned for killing a player:")
print("without shield: " + str(xp_per_dmg_point * 100) + " XP")
print("with white shield: " + str(xp_per_dmg_point * 150) + " XP")
print("with blue shield: " + str(xp_per_dmg_point * 175) + " XP")
print("with purple/gold shield: " + str(xp_per_dmg_point * 200) + " XP")
print("*assuming that you don't third party and the player dose not heal")
