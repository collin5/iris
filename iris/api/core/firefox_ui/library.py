# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from iris.api.core.pattern import Pattern


class Library(object):
    TITLE = Pattern('title.png')
    BACK_BUTTON_DISABLED = Pattern('back_button_disabled.png')
    FORWARD_BUTTON_DISABLED = Pattern('forward_button_disabled.png')
    BACK_BUTTON_ENABLED = Pattern('back_button_enabled.png')
    FORWARD_BUTTON_ENABLED = Pattern('forward_button_enabled.png')
    ORGANIZEBUTTON = Pattern('organizeButton.png')
    VIEWMENU = Pattern('viewMenu.png')
    MAINTENANCEBUTTON = Pattern('maintenanceButton.png')
    SEARCHFILTER = Pattern('searchFilter.png')
    HISTORY = Pattern('history.png')
    HISTORY_TODAY = Pattern('history_today.png')
    HISTORY_OLDER_THAN_6_MONTHS = Pattern('history_older_than_6_months.png')
    DOWNLOADS = Pattern('downloads.png')
    TAGS = Pattern('tags.png')
    ALL_BOOKMARKS = Pattern('all_bookmarks.png')
    BOOKMARKS_TOOLBAR = Pattern('bookmarks_toolbar.png')
    BOOKMARKS_MENU = Pattern('bookmarks_menu.png')
    OTHER_BOOKMARKS = Pattern('other_bookmarks.png')
    PLACESCONTENTTITLE = Pattern('placesContentTitle.png')
    PLACESCONTENTTAGS = Pattern('placesContentTags.png')
    PLACESCONTENTURL = Pattern('placesContentUrl.png')
