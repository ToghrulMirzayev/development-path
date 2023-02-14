from flask import Blueprint, render_template, request, jsonify

skills = [{"id": 1, "name": "Python", "level": "Expert"},
          {"id": 2, "name": "Flask", "level": "Intermediate"},
          {"id": 3, "name": "Javascript", "level": "Beginner"}]

manage_skills_bp = Blueprint('manage_skills', __name__)

@manage_skills_bp.route("/dev_ui")
def index():
    return render_template("dev.html", skills=skills)


@manage_skills_bp.route("/skills/<int:skill_id>", methods=['GET', 'PATCH', 'DELETE'])
def manage_skill(skill_id):
    skill = next((s for s in skills if s['id'] == skill_id), None)
    if not skill:
        return "Skill not found", 404
    
    if request.method == 'GET':
        return jsonify(skill)
    elif request.method == 'PATCH':
        data = request.get_json()
        if 'name' in data:
            skill['name'] = data['name']
        if 'level' in data:
            skill['level'] = data['level']
        return jsonify(skill)
    elif request.method == 'DELETE':
        skills.remove(skill)
        return '', 204

@manage_skills_bp.route("/skills", methods=['GET', 'POST'])
def manage_skills():
    if request.method == 'GET':
        return jsonify(skills)
    elif request.method == 'POST':
        skill = request.get_json()
        next_id = max(s['id'] for s in skills) + 1 if skills else 1
        skill['id'] = next_id
        skills.append(skill)
        return jsonify(skill), 201
