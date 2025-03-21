#!/usr/bin/python3
"""
This module defines one function: generate_invitations()
"""

import os


def generate_invitations(template, attendees):
    """
    This function generates a new invitation for each attendees.
    Args:
        template (str): The invitation template.
        attendees (list): The list of attendees.
    """
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) and \
            not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if len(template) == 0:
        print("Error: Template is empty")
        return
    if not attendees:
        print("Error: Attendees list is empty")
        return

    i = 1
    for attendee in attendees:
        invitation = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", value)

        filename = f"output_{i}.txt"

        if os.path.exists(filename):
            continue
        else:
            try:
                with open(filename, "w", encoding="UTF-8") as file:
                    file.write(invitation)
            except Exception as e:
                print(f"Error writing to {filename}: {e}")
        i += 1
