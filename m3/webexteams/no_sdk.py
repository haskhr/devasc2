#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Basic consumption of Cisco Webex Teams REST API using the
public Cisco DevNet sandbox.
"""

import requests


def main():
    """
    Execution begins here.
    """

    # Edit this depending on the message you want to post, and
    # in which room you want to post it.
    text_to_post = "Posted via Cisco Webex Teams REST API!"
    room_name = "Infrastructure TL Only"

    # Basic variables to reduce typing later. The API path is just the
    # always-on Webex Teams sandbox in DevNet. Webex Teams was formerly
    # known as Cisco Spark and I expect the URL to be updated at some
    # point to reflect the new name.
    api_path = "https://api.ciscospark.com/v1"

    # Once you sign up for Webex Teams and login, you can get your bearer
    # token here: https://developer.webex.com/docs/api/getting-started
    # The token is supplied as the value of an Authorization header.
    bearer_token = "PASTE YOUR BIG TOKEN HERE"
    headers = {"Authorization": f"Bearer {bearer_token}"}

    # Perform a GET request to get a list of all rooms in which you are
    # a member. This includes all types of rooms (private, group, etc.)
    response = requests.get(f"{api_path}/rooms", headers=headers)
    rooms = response.json()["items"]

    # Perform a basic linear search to find the specified room.
    # Print out the room name and title and store the room ID, which is
    # a large, complex string.
    internal_room_id = None
    for room in rooms:
        if room_name.lower() in room["title"].lower():
            print(f"Room ID: {room['id']}")
            print(f"Room title: {room['title']}")
            internal_room_id = room["id"]
            break

    # Assuming we found the room, issue a POST request to send the specified
    # message into the specified room. The "body" dict has to specify
    # the room ID (discovered by the previous GET request) and the text
    # we want to post.
    if internal_room_id:
        body = {"roomId": internal_room_id, "text": text_to_post}
        response = requests.post(
            f"{api_path}/messages", headers=headers, data=body
        )
        # Assuming the POST was successful, print out the text actually posted
        # along with the email address of the poster, which should be you.
        if response.ok:
            r_json = response.json()
            print(f"'{r_json['text']}' posted by '{r_json['personEmail']}'")


if __name__ == "__main__":
    main()
