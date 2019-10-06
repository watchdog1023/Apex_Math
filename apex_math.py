from __future__ import division
import os

pak_level = 45
pak_bp_s1 = 11
pak_bp_s2 = 12
pak_bp_s3 = 12
xp_per_sec = 3
xp_per_kill = 50
xp_per_dmg_point = 0.25
number_of_heirlooms = 2
average_game_time_full = float((18+21)/2) * 60
average_game_time_half = float((10+12)/2) * 60
tier_up_half_game = 54000/1300
tier_up_full_game = 54000/3000
total = pak_bp_s1 + pak_bp_s2 + pak_level + pak_bp_s3
chance = float((total/500) * 100)
wriath_heirloom_chance = float((1/number_of_heirlooms) * 100)
bloodhound_heirloom_chance = float((1/number_of_heirlooms) * 100)

print("Heirloom Chance:")
print("Next pack opened is Heirloom: " + str(chance) + "%")
print("Next pack will NOT be a Heirloom: " + str(100 - chance) + "%")
print("*assuming you finished all three battlepasses,are level 100+ and you did not buy any other packs")
print(" ")
print("Chance that Heirloom will be:")
print("Wriath's Kunai Knife: "+ str(wriath_heirloom_chance) + "%")
print("Bloodhound's Raven's Bite Axe: "+ str(bloodhound_heirloom_chance) + "%")
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
