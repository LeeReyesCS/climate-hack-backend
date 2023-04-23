from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.recycler import Recycler


recycler_bp = Blueprint('recycler', __name__, url_prefix='/recycler')

@recycler_bp.route("", methods=["GET"])
def get_all_recycles():
    
    recyclers = Recycler.query.all()
    recycler_response = []

    for recycler in recyclers:
        recycler_response.append(
            {
                'id' : recycler.recycler_id,
                'name' : recycler.name,
                'zipcode' : recycler.zipcode,
                'email' : recycler.email,
                'cans' : recycler.cans,
                'plastic': recycler.plastic,
                'glass': recycler.glass,
            }
        )
    

    return jsonify(recycler_response)



@recycler_bp.route("/<recycler_id>", methods=["GET"])
def get_one_order(recycler_id):
    order = Recycler.query.get(recycler_id)
    order_response = {"Order": order.to_dict() }
    return jsonify(order_response),200




@recycler_bp.route("", methods=["POST"])
def create_recycler():
    request_body = request.get_json()
    # if "name" not in request_body or "zipcode" not in request_body or "email" not in request_body:
    #     return jsonify({"details":"Invalid data"},400)    
    new_recycle = Recycler(
            name=request_body["name"],
            email=request_body["email"],
            zipcode=request_body["zipcode"],
            cans=request_body["cans"],
            plastic=request_body["plastic"],
            glass=request_body["glass"]
    )
    response = {"Order":new_recycle.to_dict()}

    db.session.add(new_recycle)
    db.session.commit()

    return make_response(jsonify(response),201)


@recycler_bp.route("/<recycler_id>", methods=["DELETE"])
def delete_recycler(recycler_id):
    recycler = Recycler.query.get(recycler_id)

    db.session.delete(recycler)
    db.session.commit()
    
    return {"recycler_deleted":recycler.to_dict()}