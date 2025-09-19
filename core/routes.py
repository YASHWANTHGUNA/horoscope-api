from flask import jsonify
from flask_restx import Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
from core import api
from core.utils import get_horoscope_by_day, get_horoscope_by_week, get_horoscope_by_month

ns = api.namespace('/', description='Horoscope APIs')

ZODIAC_SIGNS = {
    "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4, "Leo": 5, "Virgo": 6,
    "Libra": 7, "Scorpio": 8, "Sagittarius": 9, "Capricorn": 10,
    "Aquarius": 11, "Pisces": 12
}

# Base parser for all routes
parser = reqparse.RequestParser()
parser.add_argument('sign', type=str, required=True, help='Zodiac sign name')

# Parser for the daily route, which requires an additional 'day' argument
parser_daily = parser.copy()
parser_daily.add_argument('day', type=str, required=True,
                          help='Accepted values: Date (YYYY-MM-DD), TODAY, TOMORROW, or YESTERDAY')

class BaseHoroscopeAPI(Resource):
    """A base class that handles all common logic for horoscope endpoints."""
    parser = None
    horoscope_function = None
    requires_day_arg = False

    def get(self):
        if not self.parser or not self.horoscope_function:
            raise NotImplementedError("Subclasses must define 'parser' and 'horoscope_function'")

        args = self.parser.parse_args()
        zodiac_sign = args.get('sign')

        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]

            if self.requires_day_arg:
                day = args.get('day')
                if "-" in day:
                    datetime.strptime(day, '%Y-%m-%d')  # Validate date format
                horoscope_data = self.horoscope_function(zodiac_num, day)
            else:
                horoscope_data = self.horoscope_function(zodiac_num)

            if not horoscope_data:
                raise BadRequest("Could not retrieve horoscope data. The source website might have changed.")

            return jsonify(success=True, data=horoscope_data, status=200)

        except KeyError:
            raise NotFound('No such zodiac sign exists')
        except ValueError:
            raise BadRequest('Please enter day in the correct format: YYYY-MM-DD')

@ns.route('/get-horoscope/daily')
class DailyHoroscopeAPI(BaseHoroscopeAPI):
    """Shows daily horoscope of zodiac signs."""
    parser = parser_daily
    horoscope_function = get_horoscope_by_day
    requires_day_arg = True
    
    @ns.doc(parser=parser_daily)
    def get(self):
        return super().get()

@ns.route('/get-horoscope/weekly')
class WeeklyHoroscopeAPI(BaseHoroscopeAPI):
    """Shows weekly horoscope of zodiac signs."""
    parser = parser
    horoscope_function = get_horoscope_by_week
    
    @ns.doc(parser=parser)
    def get(self):
        return super().get()

@ns.route('/get-horoscope/monthly')
class MonthlyHoroscopeAPI(BaseHoroscopeAPI):
    """Shows monthly horoscope of zodiac signs."""
    parser = parser
    horoscope_function = get_horoscope_by_month

    @ns.doc(parser=parser)
    def get(self):
        return super().get()