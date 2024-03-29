from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from drf_sobitie.bot.constants import ABOUT_US_STATE, PROJECTS_STATE
from drf_sobitie.bot.convers_func.about_us_conversation import (
    show_about_us,
    show_documents,
    show_email_info,
    show_inclusive_workshop,
    show_ministry_reports,
    show_moscow_partala_online,
    show_projects,
    show_reports,
    show_theatre_school,
    show_inclusive_theater
)
from drf_sobitie.bot.convers_func.main_conversation import end
from drf_sobitie.bot.handlers.contacts_handler import contacts_conv
from drf_sobitie.bot.handlers.people_handler import people_conv
from drf_sobitie.bot.keyboards.about_us import (
    EMAIL_INFO,
    INCLUSIVE_WORKSHOP,
    LEGAL_DOCUMENTS,
    MOSCOW_ONLINE,
    PROJECTS,
    REPORTS,
    REPORTS_MINISTRY,
    RETURN_TO_BACK,
    THEATRE_SCHOOL,
    INCLUSIVE_THEATER
)
from drf_sobitie.bot.keyboards.main import ABOUT_US, END

about_us_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_about_us, pattern="^" + ABOUT_US + "$")],
    states={
        ABOUT_US_STATE: [
            CallbackQueryHandler(show_email_info, pattern="^" + EMAIL_INFO + "$"),
            CallbackQueryHandler(show_projects, pattern="^" + PROJECTS + "$"),
            CallbackQueryHandler(show_documents, pattern="^" + LEGAL_DOCUMENTS + "$"),
            CallbackQueryHandler(show_reports, pattern="^" + REPORTS + "$"),
            CallbackQueryHandler(
                show_ministry_reports, pattern="^" + REPORTS_MINISTRY + "$"
            ),
            contacts_conv,
            people_conv,
        ],
        PROJECTS_STATE: [
            CallbackQueryHandler(
                show_inclusive_workshop, pattern="^" + INCLUSIVE_WORKSHOP + "$"
            ),
            CallbackQueryHandler(
                show_theatre_school, pattern="^" + THEATRE_SCHOOL + "$"
            ),
            CallbackQueryHandler(
                show_moscow_partala_online, pattern="^" + MOSCOW_ONLINE + "$"
            ),
            CallbackQueryHandler(
                show_projects, pattern="^" + RETURN_TO_BACK + "$"),
            CallbackQueryHandler(
                show_inclusive_theater, pattern="^" + INCLUSIVE_THEATER + "$")
        ],
    },
    fallbacks=[CommandHandler(END, end)],
)
