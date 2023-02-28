from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.donation_conversation import (show_donations_options,
                                                        donate_with_vk,
                                                        donate_with_tinkoff,
                                                        donate_through_charity_fund,
                                                        donate_with_site_form,
                                                        go_back_to_help_menu)

from bot.convers_func.main_conversation import end
from bot.keyboards.main import END
from bot.keyboards.support import (SHOW_DONATION_OPTIONS, RETURN_TO_HELP_MENU,
                                   DONATE_WITH_SITE_FORM, DONATE_WITH_VK,
                                   DONATE_WITH_TINKOFF, DONATE_THROUGH_CHARITY_FUND)
from core.states import DONATION_OPTIONS_STATE

donation_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_donations_options,
                                       pattern='^' + SHOW_DONATION_OPTIONS + '$')],
    states={
        DONATION_OPTIONS_STATE: [
            CallbackQueryHandler(donate_with_site_form, pattern='^' + DONATE_WITH_SITE_FORM + '$'),
            CallbackQueryHandler(donate_with_vk, pattern='^' + DONATE_WITH_VK + '$'),
            CallbackQueryHandler(donate_with_tinkoff, pattern='^' + DONATE_WITH_TINKOFF + '$'),
            CallbackQueryHandler(donate_through_charity_fund,
                                 pattern='^' + DONATE_THROUGH_CHARITY_FUND + '$'),
            CallbackQueryHandler(go_back_to_help_menu,
                                 pattern='^' + RETURN_TO_HELP_MENU + '$'),
        ]
    },
    fallbacks=[CommandHandler(END, end)]
)
