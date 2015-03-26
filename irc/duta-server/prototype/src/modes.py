# Copyright (C) 2014 Christine Dodrill <shadow.h511@gmail.com> All rights reserved.
#
# This software is provided 'as-is', without any express or implied
# warranty. In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
#
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source
#    distribution.
#

FLAG_NONE           = 0x0000 # No connection flags
FLAG_REGISTERED     = 0x0001 # Registered as a client with the server
FLAG_WS_NOHANDSHAKE = 0x0002 # Websocket client that has yet to handshake

CHFL_PEON   = 0x0000 # No channel status
CHFL_VOICE  = 0x0001 # Old +v, voiced user
CHFL_HALFOP = 0x0002 # Old +h, half-operator
CHFL_CHANOP = 0x0004 # Old +o, channel operator
CHFL_ANY_OP = (CHFL_HALFOP | CHFL_CHANOP)

PROP_NONE       = 0x00000000 # No properties
PROP_MUTE       = 0x00000001 # Old +m, mute
PROP_PRIVATE    = 0x00000002 # Old +p, private channel
PROP_INVITE     = 0x00000004 # Old +i, invite only
PROP_TOPICREST  = 0x00000008 # Old +t, only ops can set topic
PROP_INTERNAL   = 0x00000010 # Old +n, only users in channel can send to it
PROP_SECRET     = 0x00000020 # Old +s, only users in channel know it exists
PROP_NOCTCP     = 0x00000040 # Old +C, no CTCP messages
PROP_NOACTION   = 0x00000080 # Old +D, no CTCP ACTION messages
PROP_NOKICKS    = 0x00000100 # Old +E, operators cannot kick
PROP_NOCAPS     = 0x00000200 # OLD +G, ALL CAPITAL LETTER MESSAGES ARE BLOCKED
PROP_NOREJOIN   = 0x00000400 # Old +J, no immediate rejoin after KICK
PROP_LARGELIST  = 0x00000800 # Old +L, larger channel lists
PROP_NOOPERKICK = 0x00001000 # Old +M, staff cannot be kicked
PROP_OPERONLY   = 0x00002000 # Old +O, only opers may join
PROP_PERMANENT  = 0x00004000 # Old +P, channel persists without users
PROP_DISFORWARD = 0x00008000 # Old +Q, channel may not be forwarded to
PROP_NONOTICE   = 0x00010000 # Old +T, channel may not be NOTICE'd to
PROP_NOCOLOR    = 0x00020000 # Old +c, channel color codes are stripped
PROP_NONICKS    = 0x00040000 # Old +d, nick changes are forbidden when in channel
PROP_FREEINVITE = 0x00080000 # Old +g, invite is freely usable
PROP_HIDEBANS   = 0x00100000 # Old +u, ban list is hidden without the proper STATUS
PROP_OPMOD      = 0x00200000 # Old +z, channel messages blocked by something are sent to ops
PROP_FREEFWD    = 0x00400000 # Old +F, free forwarding
PROP_NOREPEAT   = 0x00800000 # Old +K, no repeating messages

SET_KEY          = 0x01 # Old +k, channel key
SET_LIMIT        = 0x02 # Old +l, channel limit
SET_FORWARD      = 0x04 # Old +f, channel forward
SET_JOINTHROTTLE = 0x08 # Old +j, join throttle

LIST_BAN    = "BAN"
LIST_QUIET  = "QUIET"
LIST_EXCEPT = "EXCEPT"
LIST_INVEX  = "INVEX"

UPROP_NONE       = 0x000000
UPROP_WALLOPS    = UPROP_NONE # We do not support wallops
UPROP_LOCOPS     = UPROP_NONE # We do not support locops
UPROP_OPERWALL   = UPROP_NONE # We do not support operwall - Seriously, how many copies do you need of the same command?
UPROP_SNOMASK    = UPROP_NONE # Server notice masks are not handled by user PROPs
UPROP_BOT        = UPROP_NONE # METADATA SWHOIS can take care of this. Pointless repetition.
UPROP_INVISIBLE  = 0x000001 # Old +i, invisible client
UPROP_CALLERID   = 0x000002 # Old +g, "caller id"
UPROP_IRCOP      = 0x000004 # Old +o, user is an IRC operator
UPROP_CLOAKED    = 0x000008 # Old +x, user has a cloaked IP address
UPROP_ADMIN      = 0x000010 # Old +a, user is an IRC administrator
UPROP_OVERRIDE   = 0x000020 # Old +p, implicit chanop access
UPROP_NOCTCP     = 0x000040 # Old +C, prevents receiving CTCP messages other than ACTION (/me)
UPROP_DEAF       = 0x000080 # Old +D, ignoes all channel messages
UPROP_DISFORWARD = 0x000100 # Old +Q, prevents channel forwarding
UPROP_REGPM      = 0x000200 # Old +R, requires people to be registered with services to pm
UPROP_SOFTCALL   = 0x000400 # Old +G, Soft caller ID, caller id exempting common channels
UPROP_NOINVITE   = 0x000800 # Old +V, prevents user from getting invites
UPROP_NOSTALK    = 0x001000 # Old +I, doesn't show channel list in whois
UPROP_SSLCLIENT  = 0x002000 # Old +Z, client is connected over SSL

CHANMODES = [
    {
        "q": LIST_QUIET,
        "b": LIST_BAN,
        "e": LIST_EXCEPT,
        "I": LIST_INVEX,
    },
    {
        "k": SET_KEY,
    },
    {
        "f": SET_FORWARD,
        "l": SET_LIMIT,
        "j": SET_JOINTHROTTLE,
    },
    {
        "C": PROP_NOCTCP,
        "D": PROP_NOACTION,
        "E": PROP_NOKICKS,
        "G": PROP_NOCAPS,
        "J": PROP_NOREJOIN,
        "F": PROP_FREEFWD,
        "K": PROP_NOREPEAT,
        "L": PROP_LARGELIST,
        "M": PROP_NOOPERKICK,
        "O": PROP_OPERONLY,
        "P": PROP_PERMANENT,
        "Q": PROP_DISFORWARD,
        "T": PROP_NONOTICE,
        "c": PROP_NOCOLOR,
        "d": PROP_NONICKS,
        "g": PROP_FREEINVITE,
        "i": PROP_INVITE,
        "m": PROP_MUTE,
        "n": PROP_INTERNAL,
        "p": PROP_PRIVATE,
        "s": PROP_SECRET,
        "t": PROP_TOPICREST,
        "u": PROP_HIDEBANS,
        "z": PROP_OPMOD,
    },
    {
        "h": CHFL_HALFOP,
        "o": CHFL_CHANOP,
        "v": CHFL_VOICE,
    }
]

UMODES = {
    "i": UPROP_INVISIBLE,
    "g": UPROP_CALLERID,
    "w": UPROP_WALLOPS,
    "x": UPROP_CLOAKED,
    "o": UPROP_IRCOP,
    "a": UPROP_ADMIN,
    "l": UPROP_LOCOPS,
    "s": UPROP_SNOMASK,
    "z": UPROP_OPERWALL,
    "p": UPROP_OVERRIDE,
    "B": UPROP_BOT,
    "C": UPROP_NOCTCP,
    "D": UPROP_DEAF,
    "Q": UPROP_DISFORWARD,
    "R": UPROP_REGPM,
    "G": UPROP_SOFTCALL,
    "V": UPROP_NOINVITE,
    "I": UPROP_NOSTALK,
    "Z": UPROP_SSLCLIENT,
}

PREFIXES = {
    "+": CHFL_VOICE,
    "%": CHFL_HALFOP,
    "@": CHFL_CHANOP,
}

LISTS = {
    LIST_BAN:    "b",
    LIST_QUIET:  "q",
    LIST_EXCEPT: "e",
    LIST_INVEX:  "I",
}

STATUSES = {
    CHFL_VOICE:  "voiced",
    CHFL_HALFOP: "half-operator",
    CHFL_CHANOP: "operator",
}

PROPS = {
    PROP_NOCTCP:     "no-ctcp",
    PROP_NOACTION:   "no-action",
    PROP_NOKICKS:    "no-kicks",
    PROP_NOCAPS:     "no-caps",
    PROP_NOREJOIN:   "no-rejoin",
    PROP_FREEFWD:    "free-forward",
    PROP_NOREPEAT:   "no-repeat",
    PROP_LARGELIST:  "large-list",
    PROP_NOOPERKICK: "no-oper-kick",
    PROP_OPERONLY:   "oper-only",
    PROP_PERMANENT:  "permanent-channel",
    PROP_DISFORWARD: "disforward",
    PROP_NONOTICE:   "no-notice",
    PROP_NOCOLOR:    "no-color",
    PROP_NONICKS:    "no-nick-change",
    PROP_FREEINVITE: "free-invite",
    PROP_INVITE:     "invite-only",
    PROP_MUTE:       "muted",
    PROP_INTERNAL:   "no-external",
    PROP_PRIVATE:    "private",
    PROP_SECRET:     "secret",
    PROP_TOPICREST:  "topic-restrict",
    PROP_HIDEBANS:   "hide-bans",
    PROP_OPMOD:      "op-moderated",
}

SETS = {
    SET_KEY:          "key",
    SET_LIMIT:        "limit",
    SET_FORWARD:      "forward",
    SET_JOINTHROTTLE: "join-throttle",
}

UPROPS = {
    UPROP_INVISIBLE:  "invisible",
    UPROP_CALLERID:   "callerid",
    UPROP_CLOAKED:    "cloaked",
    UPROP_IRCOP:      "ircop",
    UPROP_ADMIN:      "admin",
    UPROP_OVERRIDE:   "override",
    UPROP_NOCTCP:     "no-ctcp",
    UPROP_DEAF:       "deaf",
    UPROP_DISFORWARD: "no-forward",
    UPROP_REGPM:      "reg-callerid",
    UPROP_SOFTCALL:   "soft-callerid",
    UPROP_NOINVITE:   "no-invites",
    UPROP_NOSTALK:    "no-stalk",
    UPROP_SSLCLIENT:  "using-ssl",
}

