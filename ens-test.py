#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask, request, jsonify
import os
import requests
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

app = Flask(__name__)



@app.route('/webhook', methods=['POST'])


def webhook_endpoint():
    data = request.get_json()

    if data.get('action_type'):
        
    # Check if the webhook action type is "created_a_lesson"
        if data.get('action_type') == 'created_a_lesson':

            # get appt id 
            return jsonify("message: ")

        else:
            return jsonifty('message: ')
    
    else:
        return jsonify({"message": "Webhook received successfully"}), 200, appointment_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


# In[ ]:




