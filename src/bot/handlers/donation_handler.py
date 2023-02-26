from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from src.bot.convers_func.donation_conversation import (show_donations_options,
                                                        donate_with_vk,
                                                        donate_with_tinkoff,
                                                        donate_through_charity_fund,
                                                        donate_with_site_form,
                                                        go_back_to_help_menu)

from src.bot.convers_func.main_conversation import end
from src.core import constants

donation_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_donations_options,
                                       pattern='^' + constants.SHOW_DONATION_OPTIONS + '$')],
    states={
        constants.DONATION_OPTIONS_STATE: [
            CallbackQueryHandler(donate_with_site_form, pattern='^' + constants.DONATE_WITH_SITE_FORM + '$'),
            CallbackQueryHandler(donate_with_vk, pattern='^' + constants.DONATE_WITH_VK + '$'),
            CallbackQueryHandler(donate_with_tinkoff, pattern='^' + constants.DONATE_WITH_TINKOFF + '$'),
            CallbackQueryHandler(donate_through_charity_fund,
                                 pattern='^' + constants.DONATE_THROUGH_CHARITY_FUND + '$'),
            CallbackQueryHandler(go_back_to_help_menu,
                                 pattern='^' + constants.RETURN_TO_HELP_MENU + '$'),
        ]
    },
    fallbacks=[CommandHandler(constants.END, end)]
)


