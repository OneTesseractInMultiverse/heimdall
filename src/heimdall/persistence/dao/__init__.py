# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, ForeignKeyConstraint, String, Table, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IsxApplication(Base):

    __tablename__ = 'isx_application'

    application_id = Column(UUID, primary_key=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    callback_url = Column(String(4000), nullable=False)
    public_key = Column(String(2048), nullable=False)
    private_key = Column(String(4096), nullable=False)
    environment = Column(String(50), nullable=False)
    configuration = Column(JSONB(astext_type=Text()))
    last_modified = Column(DateTime)
    is_enabled = Column(Boolean)

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "application_id": self.application_id,
            "name": self.name,
            "description": self.description,
            "callback_url": self.callback_url,
            "public_key": self.public_key,
            "private_key": self.private_key,
            "environment": self.environment,
            "configuration": self.configuration,
            "last_modified": self.last_modified,
            "is_enabled": self.is_enabled
        }


class IsxClaimsProvider(Base):
    __tablename__ = 'isx_claims_provider'

    provider_id = Column(UUID, primary_key=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    is_local = Column(Boolean)
    config = Column(JSONB(astext_type=Text()))
    implementation_class = Column(String(200), nullable=False)
    credentials = Column(JSONB(astext_type=Text()))

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "property_id": self.provider_id,
            "name": self.name,
            "description": self.description,
            "is_local": self.is_local,
            "config": self.config,
            "implementation_class": self.implementation_class,
            "credentials": self.credentials
        }


class IsxIdentityType(Base):
    __tablename__ = 'isx_identity_type'

    type_name = Column(String(40), primary_key=True)
    description = Column(String(256))

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "type_name": self.type_name,
            "description": self.description
        }


class IsxApplicationProvider(Base):
    __tablename__ = 'isx_application_provider'

    provider_id = Column(ForeignKey('isx_claims_provider.provider_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    created = Column(DateTime)

    application = relationship('IsxApplication')
    provider = relationship('IsxClaimsProvider')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "provider_id": self.provider_id,
            "application_id": self.application_id,
            "created": self.created
        }


class IsxClaim(Base):
    __tablename__ = 'isx_claim'

    claim_id = Column(UUID, primary_key=True, nullable=False)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    value = Column(String(512), index=True)
    description = Column(String(256))

    application = relationship('IsxApplication')
    groups = relationship('IsxGroup', secondary='isx_group_claim')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "claim_id": self.claim_id,
            "application_id": self.application_id,
            "value": self.value,
            "description": self.description
        }


class IsxGroup(Base):
    __tablename__ = 'isx_group'

    group_id = Column(UUID, primary_key=True, nullable=False)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    properties = Column(JSONB(astext_type=Text()))

    application = relationship('IsxApplication')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "group_id": self.group_id,
            "application_id": self.application_id,
            "name": self.name,
            "description": self.description,
            "properties": self.properties
        }


class IsxIdentity(Base):
    __tablename__ = 'isx_identity'

    identity_id = Column(UUID, primary_key=True)
    business_id = Column(String(40), nullable=False, unique=True)
    identity_data = Column(JSONB(astext_type=Text()))
    created = Column(DateTime)
    last_modified = Column(DateTime)
    disabled = Column(Boolean)
    type = Column(ForeignKey('isx_identity_type.type_name'), nullable=False)

    isx_identity_type = relationship('IsxIdentityType')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "identity_id": self.identity_id,
            "business_id": self.business_id,
            "identity_data": self.identity_data,
            "created": self.created,
            "last_modified": self.last_modified,
            "disabled": self.disabled,
            "type": self.type
        }


class IsxApplicationIdentity(Base):
    __tablename__ = 'isx_application_identity'

    identity_id = Column(ForeignKey('isx_identity.identity_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    created = Column(DateTime)

    application = relationship('IsxApplication')
    identity = relationship('IsxIdentity')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "identity_id": self.identity_id,
            "application_id": self.application_id,
            "created": self.created
        }


class IsxApplicationOwnership(Base):
    __tablename__ = 'isx_application_ownership'

    identity_id = Column(ForeignKey('isx_identity.identity_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    created = Column(DateTime)
    from_date = Column(DateTime)
    until_date = Column(DateTime)
    is_owner = Column(Boolean)
    is_manager = Column(Boolean)
    configuration = Column(JSONB(astext_type=Text()))

    application = relationship('IsxApplication')
    identity = relationship('IsxIdentity')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "identity_id": self.identity_id,
            "application_id": self.application_id,
            "created": self.created,
            "from_date": self.from_date,
            "until_date": self.until_date,
            "is_owner": self.is_owner,
            "is_manager": self.is_manager,
            "configuration": self.configuration
        }


class IsxGroupClaim(Base):
    __tablename__ = 'isx_group_claim'
    __table_args__ = (
        ForeignKeyConstraint(['claim_id', 'application_id'], ['isx_claim.claim_id', 'isx_claim.application_id'], ondelete='CASCADE'),
        ForeignKeyConstraint(['group_id', 'application_id'], ['isx_group.group_id', 'isx_group.application_id'], ondelete='CASCADE')
    )

    group_id = Column(UUID, primary_key=True, nullable=False, index=True)
    claim_id = Column(UUID, primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)

    application = relationship('IsxApplication')
    claim = relationship('IsxClaim')
    group = relationship('IsxGroup')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "group_id": self.group_id,
            "claim_id": self.claim_id,
            "application_id": self.application_id
        }


class IsxIdentityClaim(Base):
    __tablename__ = 'isx_identity_claim'
    __table_args__ = (
        ForeignKeyConstraint(['claim_id', 'application_id'], ['isx_claim.claim_id', 'isx_claim.application_id'], ondelete='CASCADE'),
    )

    claim_id = Column(UUID, primary_key=True, nullable=False, index=True)
    application_id = Column(UUID, primary_key=True, nullable=False, index=True)
    identity_id = Column(ForeignKey('isx_identity.identity_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    from_date = Column(DateTime)
    until_date = Column(DateTime)

    claim = relationship('IsxClaim')
    identity = relationship('IsxIdentity')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "claim_id": self.claim_id,
            "application_id": self.application_id,
            "identity_id": self.identity_id,
            "from_date": self.from_date,
            "until_date": self.until_date
        }


class IsxIdentityGroup(Base):
    __tablename__ = 'isx_identity_group'
    __table_args__ = (
        ForeignKeyConstraint(['group_id', 'application_id'], ['isx_group.group_id', 'isx_group.application_id'], ondelete='CASCADE'),
    )

    group_id = Column(UUID, primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    identity_id = Column(ForeignKey('isx_identity.identity_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)

    application = relationship('IsxApplication')
    group = relationship('IsxGroup')
    identity = relationship('IsxIdentity')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "group_id": self.group_id,
            "application_id": self.application_id,
            "identity_id": self.identity_id
        }

class IsxProfile(Base):
    __tablename__ = 'isx_profile'

    identity_id = Column(ForeignKey('isx_identity.identity_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    profile_data = Column(JSONB(astext_type=Text()))

    application = relationship('IsxApplication')
    identity = relationship('IsxIdentity')

    # -------------------------------------------------------------------------
    # PROPERTY DICTIONARY
    # -------------------------------------------------------------------------
    @property
    def dictionary(self):
        return {
            "identity_id": self.identity_id,
            "application_id": self.application_id,
            "profile_data": self.profile_data
        }


isx_view_application_identity = Table(
    'isx_view_application_identity', metadata,
    Column('identity_id', UUID),
    Column('business_id', String(40)),
    Column('application_id', UUID),
    Column('name', String(40))
)


isx_view_application_owned = Table(
    'isx_view_application_owned', metadata,
    Column('identity_id', UUID),
    Column('business_id', String(40)),
    Column('application_id', UUID),
    Column('name', String(40)),
    Column('is_manager', Boolean),
    Column('is_owner', Boolean)
)


isx_view_application_provider = Table(
    'isx_view_application_provider', metadata,
    Column('application_id', UUID),
    Column('provider_id', UUID),
    Column('name', String(40)),
    Column('description', String(256))
)


isx_view_identity_application_type = Table(
    'isx_view_identity_application_type', metadata,
    Column('application_id', UUID),
    Column('type', String(40)),
    Column('identity_count', BigInteger)
)


isx_view_identity_claim = Table(
    'isx_view_identity_claim', metadata,
    Column('identity_id', UUID),
    Column('claim_id', UUID),
    Column('application_id', UUID)
)


isx_view_identity_group = Table(
    'isx_view_identity_group', metadata,
    Column('identity_id', UUID),
    Column('business_id', String(40)),
    Column('type', String(40)),
    Column('application_id', UUID),
    Column('group_id', UUID),
    Column('name', String(40)),
    Column('description', String(256)),
    Column('properties', JSONB(astext_type=Text()))
)


isx_view_identity_group_claim = Table(
    'isx_view_identity_group_claim', metadata,
    Column('identity_id', UUID),
    Column('business_id', String(40)),
    Column('type', String(40)),
    Column('application_id', UUID),
    Column('group_id', UUID),
    Column('name', String(40)),
    Column('claim_id', UUID),
    Column('value', String(512)),
    Column('description', String(256))
)


isx_view_profile_identity = Table(
    'isx_view_profile_identity', metadata,
    Column('identity_id', UUID),
    Column('business_id', String(40)),
    Column('profile_data', JSONB(astext_type=Text())),
    Column('application_id', UUID),
    Column('name', String(40))
)
