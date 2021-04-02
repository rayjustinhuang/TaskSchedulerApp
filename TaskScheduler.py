# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:32:08 2021

@author: Ray Justin Huang
"""

import itertools
from collections import namedtuple, defaultdict

# Instance variables
Task = namedtuple('Task', ['name', 'duration', 'blocks'])

def task_subdivider(tasks: list):
    duration_dict = {}
    for task in tasks:
        duration_dict[task.name] = task.duration / task.blocks
    return duration_dict

def task_combinations(tasks: list):
    task_strings = []
    total_blocks = sum(task.blocks for task in tasks)
    for task in tasks:
        task_strings += [task.name] * task.blocks
    
    combo_list = []
    for i in range(1, total_blocks+1):
        combo_list += list(itertools.combinations(task_strings, i))
        
    return tuple(combo_list)

def combination_duration(hours_in_day: float, combi_tuple: tuple, duration_dict: dict):
    viable_sequences = defaultdict(list)
    for combination in combi_tuple:
        total_duration = sum(duration_dict[i] for i in combination)
        if total_duration > hours_in_day:
            continue
        else:
            time_left = hours_in_day - total_duration
            viable_sequences[time_left].append(combination)
            
    min_time = min(viable_sequences.keys())
    
    return viable_sequences[min_time], hours_in_day - min_time

def printing_format(sequence_list: list, min_time: float):
    print('The viable sequences are {} hours long:'.format(min_time))
    for sequence in sequence_list:
        print(sequence)

if __name__ == '__main__':
    task_list = [
        Task('emails', 2, 3),
        Task('meeting', 1, 1),
        Task('break', 1, 4),
        Task('Excel', 2, 2),
        Task('PowerPoint', 2, 2),
        ]
    
    hours_in_day = 8
    
    durations = task_subdivider(task_list)
    
    combos = task_combinations(task_list)
    
    viable_sequence, minimized_time = combination_duration(hours_in_day, combos, durations)
    
    printing_format(viable_sequence, minimized_time)