# Copyright 2014-2016 OpenMarket Ltd
# Copyright 2017 Vector Creations Ltd
# Copyright 2018-2019 New Vector Ltd
# Copyright 2019 The Matrix.org Foundation C.I.C.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#################################################################
# NOTICE OF MODIFICATION:
# * This file has been modified from its original version.
# * This notice has been added with the purpose of meeting the
#   requirements of the Apache License 2.0.
#################################################################


"""Contains constants from the specification."""

import enum
from typing import Final

# the max size of a (canonical-json-encoded) event
MAX_PDU_SIZE = 65536

# the "depth" field on events is limited to 2**63 - 1
MAX_DEPTH = 2**63 - 1

# the maximum length for a room alias is 255 characters
MAX_ALIAS_LENGTH = 255

# the maximum length for a user id is 255 characters
MAX_USERID_LENGTH = 255

# Constant value used for the pseudo-thread which is the main timeline.
MAIN_TIMELINE: Final = "main"


class Membership:

    """Represents the membership states of a user in a room."""

    INVITE: Final = "invite"
    JOIN: Final = "join"
    KNOCK: Final = "knock"
    LEAVE: Final = "leave"
    BAN: Final = "ban"
    LIST: Final = (INVITE, JOIN, KNOCK, LEAVE, BAN)


class PresenceState:
    """Represents the presence state of a user."""

    OFFLINE: Final = "offline"
    UNAVAILABLE: Final = "unavailable"
    ONLINE: Final = "online"
    BUSY: Final = "org.matrix.msc3026.busy"


class JoinRules:
    PUBLIC: Final = "public"
    KNOCK: Final = "knock"
    INVITE: Final = "invite"
    PRIVATE: Final = "private"
    # As defined for MSC3083.
    RESTRICTED: Final = "restricted"
    # As defined for MSC3787.
    KNOCK_RESTRICTED: Final = "knock_restricted"


class RestrictedJoinRuleTypes:
    """Understood types for the allow rules in restricted join rules."""

    ROOM_MEMBERSHIP: Final = "m.room_membership"


class LoginType:
    PASSWORD: Final = "m.login.password"
    EMAIL_IDENTITY: Final = "m.login.email.identity"
    MSISDN: Final = "m.login.msisdn"
    RECAPTCHA: Final = "m.login.recaptcha"
    TERMS: Final = "m.login.terms"
    SSO: Final = "m.login.sso"
    DUMMY: Final = "m.login.dummy"
    REGISTRATION_TOKEN: Final = "m.login.registration_token"
    SIOPv2 = "m.login.siopv2"


# This is used in the `type` parameter for /register when called by
# an appservice to register a new user.
APP_SERVICE_REGISTRATION_TYPE: Final = "m.login.application_service"


class EventTypes:
    Member: Final = "m.room.member"
    Create: Final = "m.room.create"
    Tombstone: Final = "m.room.tombstone"
    JoinRules: Final = "m.room.join_rules"
    PowerLevels: Final = "m.room.power_levels"
    Aliases: Final = "m.room.aliases"
    Redaction: Final = "m.room.redaction"
    ThirdPartyInvite: Final = "m.room.third_party_invite"

    RoomHistoryVisibility: Final = "m.room.history_visibility"
    CanonicalAlias: Final = "m.room.canonical_alias"
    Encrypted: Final = "m.room.encrypted"
    RoomAvatar: Final = "m.room.avatar"
    RoomEncryption: Final = "m.room.encryption"
    GuestAccess: Final = "m.room.guest_access"

    # These are used for validation
    Message: Final = "m.room.message"
    Topic: Final = "m.room.topic"
    Name: Final = "m.room.name"

    ServerACL: Final = "m.room.server_acl"
    Pinned: Final = "m.room.pinned_events"

    Retention: Final = "m.room.retention"

    Dummy: Final = "org.matrix.dummy_event"

    SpaceChild: Final = "m.space.child"
    SpaceParent: Final = "m.space.parent"

    Reaction: Final = "m.reaction"


class ToDeviceEventTypes:
    RoomKeyRequest: Final = "m.room_key_request"


class DeviceKeyAlgorithms:
    """Spec'd algorithms for the generation of per-device keys"""

    ED25519: Final = "ed25519"
    CURVE25519: Final = "curve25519"
    SIGNED_CURVE25519: Final = "signed_curve25519"


class EduTypes:
    PRESENCE: Final = "m.presence"
    TYPING: Final = "m.typing"
    RECEIPT: Final = "m.receipt"
    DEVICE_LIST_UPDATE: Final = "m.device_list_update"
    SIGNING_KEY_UPDATE: Final = "m.signing_key_update"
    UNSTABLE_SIGNING_KEY_UPDATE: Final = "org.matrix.signing_key_update"
    DIRECT_TO_DEVICE: Final = "m.direct_to_device"


class RejectedReason:
    AUTH_ERROR: Final = "auth_error"
    OVERSIZED_EVENT: Final = "oversized_event"


class RoomCreationPreset:
    PRIVATE_CHAT: Final = "private_chat"
    PUBLIC_CHAT: Final = "public_chat"
    TRUSTED_PRIVATE_CHAT: Final = "trusted_private_chat"


class ThirdPartyEntityKind:
    USER: Final = "user"
    LOCATION: Final = "location"


ServerNoticeMsgType: Final = "m.server_notice"
ServerNoticeLimitReached: Final = "m.server_notice.usage_limit_reached"


class UserTypes:
    """Allows for user type specific behaviour. With the benefit of hindsight
    'admin' and 'guest' users should also be UserTypes. Normal users are type None
    """

    SUPPORT: Final = "support"
    BOT: Final = "bot"
    ALL_USER_TYPES: Final = (SUPPORT, BOT)


class RelationTypes:
    """The types of relations known to this server."""

    ANNOTATION: Final = "m.annotation"
    REPLACE: Final = "m.replace"
    REFERENCE: Final = "m.reference"
    THREAD: Final = "m.thread"


class LimitBlockingTypes:
    """Reasons that a server may be blocked"""

    MONTHLY_ACTIVE_USER: Final = "monthly_active_user"
    HS_DISABLED: Final = "hs_disabled"


class EventContentFields:
    """Fields found in events' content, regardless of type."""

    # Labels for the event, cf https://github.com/matrix-org/matrix-doc/pull/2326
    LABELS: Final = "org.matrix.labels"

    # Timestamp to delete the event after
    # cf https://github.com/matrix-org/matrix-doc/pull/2228
    SELF_DESTRUCT_AFTER: Final = "org.matrix.self_destruct_after"

    # cf https://github.com/matrix-org/matrix-doc/pull/1772
    ROOM_TYPE: Final = "type"

    # Whether a room can federate.
    FEDERATE: Final = "m.federate"

    # The creator of the room, as used in `m.room.create` events.
    #
    # This is deprecated in MSC2175.
    ROOM_CREATOR: Final = "creator"

    # Used in m.room.guest_access events.
    GUEST_ACCESS: Final = "guest_access"

    # The authorising user for joining a restricted room.
    AUTHORISING_USER: Final = "join_authorised_via_users_server"

    # Use for mentioning users.
    MENTIONS: Final = "m.mentions"

    # an unspecced field added to to-device messages to identify them uniquely-ish
    TO_DEVICE_MSGID: Final = "org.matrix.msgid"


class RoomTypes:
    """Understood values of the room_type field of m.room.create events."""

    SPACE: Final = "m.space"


class RoomEncryptionAlgorithms:
    MEGOLM_V1_AES_SHA2: Final = "m.megolm.v1.aes-sha2"
    DEFAULT: Final = MEGOLM_V1_AES_SHA2


class AccountDataTypes:
    DIRECT: Final = "m.direct"
    IGNORED_USER_LIST: Final = "m.ignored_user_list"
    TAG: Final = "m.tag"
    PUSH_RULES: Final = "m.push_rules"


class HistoryVisibility:
    INVITED: Final = "invited"
    JOINED: Final = "joined"
    SHARED: Final = "shared"
    WORLD_READABLE: Final = "world_readable"


class GuestAccess:
    CAN_JOIN: Final = "can_join"
    # anything that is not "can_join" is considered "forbidden", but for completeness:
    FORBIDDEN: Final = "forbidden"


class ReceiptTypes:
    READ: Final = "m.read"
    READ_PRIVATE: Final = "m.read.private"
    FULLY_READ: Final = "m.fully_read"


class PublicRoomsFilterFields:
    """Fields in the search filter for `/publicRooms` that we understand.

    As defined in https://spec.matrix.org/v1.3/client-server-api/#post_matrixclientv3publicrooms
    """

    GENERIC_SEARCH_TERM: Final = "generic_search_term"
    ROOM_TYPES: Final = "room_types"


class ApprovalNoticeMedium:
    """Identifier for the medium this server will use to serve notice of approval for a
    specific user's registration.

    As defined in https://github.com/matrix-org/matrix-spec-proposals/blob/babolivier/m_not_approved/proposals/3866-user-not-approved-error.md
    """

    NONE = "org.matrix.msc3866.none"
    EMAIL = "org.matrix.msc3866.email"


class Direction(enum.Enum):
    BACKWARDS = "b"
    FORWARDS = "f"


class VPSessionStatus(enum.Enum):
    CREATED = "created"
    POSTED = "posted"
    INVALIDATED = "invalidated"


class SIOPv2SessionStatus(enum.Enum):
    CREATED = "created"
    POSTED = "posted"
    AUTHORIZED = "authorized"
    INVALIDATED = "invalidated"


class VPType(enum.Enum):
    AGE_OVER_13 = "ageOver13"
    AFFILIATION = "affiliation"
    JOIN_CONFERENCE = "joinConference"

    @property
    def description_ja(self):
        if self.value == "ageOver13":
            return "13歳以上であること"
        if self.value == "affiliation":
            return "所属組織の情報"
        if self.value == "joinConference":
            return "イベント参加"