register(GRAMPLET,
         id="HistContext", 
         name=_("Historical Context"),
         description = _("Displaying a historical context"),
         status = STABLE,
         version = '0.2.10',
         fname="HistContext.py",
         height = 20,
         detached_width = 510,
         detached_height = 480,
         expand = True,
         gramplet = "HistContext",
         gramplet_title=_("Historical Context"),
         gramps_target_version="5.2",
         help_url="https://github.com/kajmikkelsen/TimeLineGramplet",
         navtypes=["Person","Dashboard"],
         include_in_listing = True,
         )
