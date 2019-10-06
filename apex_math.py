from __future__ import division
import os

pak_level = 45
pak_bp_s1 = 11
pak_bp_s2 = 12
pak_bp_s3 = 12
number_of_heirlooms = 2
average_game_time_full = float((18+22)/2)
average_game_time_half = float((11+13)/2)
tier_up_half_game = 54000/1300
tier_up_full_game = 54000/3000
total = pak_bp_s1 + pak_bp_s2 + pak_level
chance = float((total/500)*100)
wriath_heirloom_chance = float((1/number_of_heirlooms)*100)
bloodhound_heirloom_chance = float((1/number_of_heirlooms)*100)

print("Heirloom Chance:")
print("Next pack opened is Heirloom: " + str(chance) + "%")
print("Next pack will NOT be a Heirloom: " + str(100 - chance) + "%")
print(" ")
print("Chance that Heirloom will be:")
print("Wriath's Kunai Knife: "+ str(wriath_heirloom_chance) + "%")
print("Bloodhound's Raven's Bite Axe: "+ str(bloodhound_heirloom_chance) + "%")
print(" ")
'''print("Battlepass S2 time to \"tier\" up:")
print("Level 17 onwards: ")
print("Full Game(Top 3):")
print(str(round(float(tier_up_full_game) * average_game_time_full,0)) + " Minutes")
print(str(round(float(tier_up_full_game) * average_game_time_full,0)/60) + " Hours")
print("Half Game(Top 10):")
print(str(round(float(tier_up_half_game) * average_game_time_half,0)) + " Minutes")
print(str(round(float(tier_up_half_game) * average_game_time_half,0)/60) + " Hours")'''
