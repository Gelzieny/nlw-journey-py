from flask import Blueprint, jsonify, request

from controllers.activity_controller import ActivityController
from controllers.link_controller import LinkController
from controllers.participants_controller import PartController
from controllers.trip_controller import TripController
from models.repositories.activity_repository import ActivityRepository
from models.repositories.links_repository import LinksRepository
from models.repositories.participants_repository import ParticipantsRepository
from models.repositories.trips_repository import TripsRepository
from models.repositories.email_repository import EmailsRepository
from models.settings.db_connection_handle import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
  conn = db_connection_handler.get_connection()
  trip_repo = TripsRepository(conn)
  email_repo = EmailsRepository(conn)

  controller = TripController(trip_repository=trip_repo, email_repository=email_repo)

  response = controller.create(request.json)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/list", methods=["GET"])
def find_trip_details():
  conn = db_connection_handler.get_connection()
  trip_repo = TripsRepository(conn)

  controller = TripController(trip_repository=trip_repo)

  response = controller.find_trip_details()
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip_by_id(tripId):
  conn = db_connection_handler.get_connection()
  trip_repo = TripsRepository(conn)

  controller = TripController(trip_repository=trip_repo)

  response = controller.find_trip_by_id(tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def trip_confirm(tripId):
  conn = db_connection_handler.get_connection()
  trip_repo = TripsRepository(conn)

  controller = TripController(trip_repository=trip_repo)

  response = controller.trip_confirm(tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
  conn = db_connection_handler.get_connection()
  link_repo = LinksRepository(conn)

  controller = LinkController(link_repository=link_repo)

  response = controller.create(request.json, tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
  conn = db_connection_handler.get_connection()
  link_repo = LinksRepository(conn)

  controller = LinkController(link_repository=link_repo)

  response = controller.find_link_by_id(tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
  conn = db_connection_handler.get_connection()
  part_repo = ParticipantsRepository(conn)
  email_repo = EmailsRepository(conn)

  controller = PartController(part_repository=part_repo, email_repository=email_repo)

  response = controller.create(request.json, tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
  conn = db_connection_handler.get_connection()
  act_repo = ActivityRepository(conn)

  controller = ActivityController(activity_repository=act_repo)

  response = controller.create(request.json, tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
  conn = db_connection_handler.get_connection()
  part_repo = ParticipantsRepository(conn)

  controller = PartController(part_repository=part_repo)

  response = controller.find_part_by_id(tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
  conn = db_connection_handler.get_connection()
  act_repo = ActivityRepository(conn)

  controller = ActivityController(activity_repository=act_repo)

  response = controller.find_from_trip(tripId)
  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/participant/<participantpId>/confirm", methods=["GET"])
def participant_confirm(participantpId):
  conn = db_connection_handler.get_connection()
  part_repo = ParticipantsRepository(conn)

  controller = PartController(part_repository=part_repo)

  response = controller.part_confirm(participantpId)
  return jsonify(response["body"]), response["status_code"]

