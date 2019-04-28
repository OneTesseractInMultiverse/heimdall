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


class IsxClaimsProvider(Base):
    __tablename__ = 'isx_claims_provider'

    provider_id = Column(UUID, primary_key=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    is_local = Column(Boolean)
    config = Column(JSONB(astext_type=Text()))
    implementation_class = Column(String(200), nullable=False)
    credentials = Column(JSONB(astext_type=Text()))


class IsxIdentityType(Base):
    __tablename__ = 'isx_identity_type'

    type_name = Column(String(40), primary_key=True)
    description = Column(String(256))


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


class IsxApplicationProvider(Base):
    __tablename__ = 'isx_application_provider'

    provider_id = Column(ForeignKey('isx_claims_provider.provider_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    created = Column(DateTime)

    application = relationship('IsxApplication')
    provider = relationship('IsxClaimsProvider')


class IsxClaim(Base):
    __tablename__ = 'isx_claim'

    claim_id = Column(UUID, primary_key=True, nullable=False)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    value = Column(String(512), index=True)
    description = Column(String(256))

    application = relationship('IsxApplication')
    groups = relationship('IsxGroup', secondary='isx_group_claim')


class IsxGroup(Base):
    __tablename__ = 'isx_group'

    group_id = Column(UUID, primary_key=True, nullable=False)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    properties = Column(JSONB(astext_type=Text()))

    application = relationship('IsxApplication')


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


class IsxApplicationIdentity(Base):
    __tablename__ = 'isx_application_identity'

    identity_id = Column(ForeignKey('isx_identity.identity_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    created = Column(DateTime)

    application = relationship('IsxApplication')
    identity = relationship('IsxIdentity')


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


isx_group_claim = Table(
    'isx_group_claim', metadata,
    Column('claim_id', UUID, primary_key=True, nullable=False),
    Column('group_id', UUID, primary_key=True, nullable=False, index=True),
    Column('application_id', UUID, primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['claim_id', 'application_id'], ['isx_claim.claim_id', 'isx_claim.application_id'], ondelete='CASCADE'),
    ForeignKeyConstraint(['group_id', 'application_id'], ['isx_group.group_id', 'isx_group.application_id'], ondelete='CASCADE')
)


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


class IsxProfile(Base):
    __tablename__ = 'isx_profile'

    identity_id = Column(ForeignKey('isx_identity.identity_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    application_id = Column(ForeignKey('isx_application.application_id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    profile_data = Column(JSONB(astext_type=Text()))

    application = relationship('IsxApplication')
    identity = relationship('IsxIdentity')
