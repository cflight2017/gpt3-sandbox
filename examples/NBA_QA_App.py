#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 6 17:53:39 2020
@author: christienwright
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ['OPENAI_CONFIG'] = '/Users/christienwright/gpt3-sandbox/openai.cfg'
os.environ['FLASK_APP'] = '/Users/christienwright/gpt3-sandbox/NBA_QA_App.py'
os.environ['FLASK_ENV'] = 'development'
from api import demo_web_app
from api import GPT, Example, UIConfig

question_prefix = 'Q: '
question_suffix = "\n"
answer_prefix = "A: "
answer_suffix = "\n\n"


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.75,
          max_tokens=100,
          input_prefix=question_prefix,
          input_suffix=question_suffix,
          output_prefix=answer_prefix,
          output_suffix=answer_suffix,
          append_output_prefix_to_query=True)

gpt.add_example(Example('Who leads the NBA in points?',
                        'James Harden'))
gpt.add_example(
    Example('Who leads the NBA in assists?', 'LeBron James'))

gpt.add_example(Example(
    'Who won the NBA championship in 2019?', 'The Toronto Raptors won the NBA championship in 2019'))

gpt.add_example(Example('Who led the NBA in rebounds in 2020?',
                        'Andre Drummond'))

gpt.add_example(Example('Who won the NBA slam dunk contest in 2019?',
                        'Hamidou Diallo'))

gpt.add_example(Example('Who won the 3-point shootout in 2019?',
                        'Joe Harris'))


gpt.add_example(Example('Who won the skills competition in 2019?',
                        'Jayson Tatum'))


gpt.add_example(Example('Who won the NBA All-Star game?',
                        'Team LeBron'))

gpt.add_example(Example('Who was the MVP of the NBA All-Star game in 2019?',
                        'Kevin Durant'))

gpt.add_example(Example('Who was the rookie of the year in 2019?',
                        'Luka Doncic'))

gpt.add_example(Example('Who was the MVP of the NBA Finals in 2019?',
                        'Kawhi Leonard'))

gpt.add_example(Example('Who was the Defensive Player of the Year in 2019?',
                        'Rudy Gobert'))

gpt.add_example(Example('Who was the 6th man of the year in 2019?',
                        'Lou Williams'))


gpt.add_example(Example('Who was the MVP of the NBA in 2019?',
                        'Giannis Antetokounmpo'))

gpt.add_example(Example('Who won the NBA Championship in 2018?',
                        'Golden State Warriors'))

gpt.add_example(Example('Who won the NBA slam dunk contest in 2018?',
                        'Donovan Mitchell'))

gpt.add_example(Example('Who won the 3-point shootout in 2019?',
                        'Devin Booker'))

gpt.add_example(Example('Who won the skills competition in 2018?',
                        'Spencer Dinwiddie'))

gpt.add_example(Example('Who is the commissioner of the NBA?',
                        'Adam Silver'))

gpt.add_example(Example('Who was the MVP of the NBA All-Star game in 2018?',
                        'LeBron James'))

gpt.add_example(Example('Who was the rookie of the year in 2018?',
                        'Ben Simmons'))

gpt.add_example(Example('Who was the NBA Finals MVP in 2018?',
                        'Kevin Durant'))

gpt.add_example(Example('Who was the Defensive Player of the Year in 2018?',
                        'Rudy Gobert'))

gpt.add_example(Example('Who was the 6th man of the year in 2018?',
                        'Lou Williams'))

gpt.add_example(Example('Who was the MVP of the NBA in 2018?',
                        'James Harden'))
                        
gpt.add_example(Example('Who won the NBA Championship in 2004?',
                        'Detroit Pistons'))
                        






# Define UI configuration
config = UIConfig(description="NBA Fan Q&A",
                  button_text="Answer",
                  placeholder="Who's the 2019 MVP?")

demo_web_app(gpt, config)
