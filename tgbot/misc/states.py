from aiogram.fsm.state import StatesGroup, State

class AdminSelecting(StatesGroup):
    get_paysystem_name = State()
    get_card_number = State()
    get_card_description = State()
    choosing_job_name = State()
    choosing_affiliate_name = State()


class UserSelecting(StatesGroup):
    choosing_city_name = State()
    choosing_job_name = State()
    choosing_affiliate_name = State()

