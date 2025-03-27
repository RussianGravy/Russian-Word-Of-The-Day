# Russian Word Of The Day (Email Server)

## Overview

This project automates the process of learning Russian vocabulary by sending a daily email with a new word and its definition. It leverages the Gemini LLM to generate vocabulary and uses cron jobs on a Raspberry Pi to schedule the email delivery and weekly topic updates.

## How It Works

1.  **Vocabulary Generation:** A Python script prompts the Gemini LLM for new Russian words based on the week's topic. 
2.  **Email Delivery:** Another script emails me the words using the Gmail SMTP server.
3.  **Automation:** A cron job on my Raspberry Pi executes those scripts daily; another cron job updates the topic weekly.

## Why I Built It

This project was born out of a desire to streamline the Russian vocabulary learning process. The inspiration to learn Russian stems from:

* **Rich History:** An appreciation for the country's historical significance.
* **Family Ancestry:** A connection to Russian heritage.
* **Interpersonal Connection:** The desire to communicate with Russian speakers.

## What I Learned

Building this project provided valuable experience in:

* **AI Prompt Optimization:** Refining prompts to elicit relevant and accurate vocabulary from the Gemini LLM.
* **Cron Job Implementation:** Learning to schedule and manage automated tasks on a Raspberry Pi using cron jobs.
