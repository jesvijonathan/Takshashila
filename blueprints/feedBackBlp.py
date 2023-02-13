from flask import request
from flask.views import MethodView

from flask_smorest import Blueprint

from controllers.feedbackController import createFeedBack, getFeedBack

feedBackBlp = Blueprint("feedBackBlp", __name__, url_prefix='/api')


@feedBackBlp.route("/feedback")
class FeedBack(MethodView):
    def get(self):
        return getFeedBack()

    def post(self):

        return createFeedBack(request.get_json())
        # return request.get_json()
