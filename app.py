# main.py (on Railway) - CODE FOR THE '/join' API ENDPOINT

# Assuming 'app' is the Flask object defined at the top of main.py
# and 'sendEmote' is the function that actually sends the command to the game server.

@app.route('/join', methods=['GET'])
def join_team_route():
    try:
        # The parameters come from the Vercel proxy
        emote_id = request.args.get('emote_id')
        team_code = request.args.get('tc')
        
        # Collect all uids (uid1, uid2, uid3, uid4)
        uids = []
        for i in range(1, 5):
            uid = request.args.get(f'uid{i}')
            if uid:
                uids.append(uid)

        if not all([team_code, emote_id, uids]):
            # Always return a clear JSON error
            return jsonify({"status": "error", "message": "Missing team_code, emote_id, or UIDs in the request."}), 400

        # --- YOUR CORE BOT LOGIC TO PROCESS THE REQUEST GOES HERE ---
        # Example: sendEmote(emote_id, team_code, uids) 
        # (You need to ensure this is correctly integrated with your asyncio loop)
        
        # --- FIX #2: Return a guaranteed JSON response upon success ---
        return jsonify({
            "status": "success", 
            "message": f"Emote {emote_id} command was received and processed for team {team_code}"
        }), 200
        # --- END FIX ---

    except Exception as e:
        # Catch any internal errors and return JSON
        return jsonify({"status": "error", "message": f"Internal Bot API Error: {str(e)}"}), 500

# NOTE: Keep the rest of your main.py code (asyncio loop, flask thread startup)
# as you need it for your Railway deployment.
