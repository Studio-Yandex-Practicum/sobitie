from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.about_us_conversation import (show_about_us,
                                                    show_documents,
                                                    show_inclusive_theatre,
                                                    show_inclusive_workshop,
                                                    show_ministry_reports,
                                                    show_theatre_school,
                                                    show_projects,
                                                    show_reports)
from bot.convers_func.main_conversation import end
from bot.keyboards.main import ABOUT_US, END
from bot.keyboards.about_us import (INCLUSIVE_THEATRE,
                                    INCLUSIVE_WORKSHOP,
                                    LEGAL_DOCUMENTS,
                                    PROJECTS,
                                    REPORTS,
                                    REPORTS_MINISTRY,
                                    RETURN_TO_ABOUT_US,
                                    RETURN_TO_BACK, THEATRE_SCHOOL)
from core.states import ABOUT_US_STATE, PROJECTS_STATE
from bot.handlers.contacts_handler import contacts_conv
from bot.handlers.people_handler import people_conv


about_us_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_about_us, pattern='^' + ABOUT_US + '$')],
    states={
        ABOUT_US_STATE: [
            CallbackQueryHandler(show_projects, pattern='^' + PROJECTS + '$'),
            CallbackQueryHandler(show_documents, pattern='^' + LEGAL_DOCUMENTS + '$'),
            CallbackQueryHandler(show_reports, pattern='^' + REPORTS + '$'),
            CallbackQueryHandler(show_ministry_reports, pattern='^' + REPORTS_MINISTRY + '$'),
            contacts_conv,
            people_conv,
        ],
        PROJECTS_STATE: [
            CallbackQueryHandler(show_about_us, pattern='^' + RETURN_TO_ABOUT_US + '$'),
            CallbackQueryHandler(show_inclusive_theatre, pattern='^' + INCLUSIVE_THEATRE + '$'),
            CallbackQueryHandler(show_inclusive_workshop, pattern='^' + INCLUSIVE_WORKSHOP + '$'),
            CallbackQueryHandler(show_theatre_school, pattern='^' + THEATRE_SCHOOL + '$'),
            CallbackQueryHandler(show_projects, pattern='^' + RETURN_TO_BACK + '$')
        ],
    },
    fallbacks=[CommandHandler(END, end)]
)
