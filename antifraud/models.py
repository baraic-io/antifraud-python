import uuid
import datetime

from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    source_user_id: str | None = None
    source_identifier: str | None = None
    source_fullname: str | None = None
    source_card_number: str | None = None
    source_account: str | None = None
    target_user_id: str | None = None
    target_identifier: str | None = None
    target_fullname: str | None = None
    target_card_number: str | None = None
    target_account: str | None = None
    merchant_id: str | None = None
    merchant_terminal_id: str | None = None
    merchant_mcc_code: str | None = None
    date: datetime.datetime | None = None
    time: datetime.time | None = None
    amount: str | None = None
    currency: str | None = None
    payment_mode: str | None = None
    transaction_type: str | None = None
    transaction_country: str | None = None
    transaction_city: str | None = None
    transaction_channel: str | None = None
    transaction_rrn: str | None = None
    card_type: str | None = None
    device_id: str | None = None


class AFTransaction(BaseModel):
    transaction: Transaction
    af_id: uuid.UUID | None = None


class SyncResolution(BaseModel):
    af_transaction: AFTransaction
    af_id: str | None = None
    af_error: str | None = None
    af_details: dict | None = None
    af_finalized_date: datetime.datetime | None = None
    af_finalized_action: str | None = None
    af_process_time: int | None = None
    af_validated_services: list[str] | None = None
    af_unvalidated_services: list[str] | None = None
    af_retry_attempt: int | None = None
    af_fraud: bool | None = None
    af_blocked: bool | None = None
    af_validated: bool | None = None
    af_alert: bool | None = None


class AsyncResolution(BaseModel):
    af_id: str | None = None
    af_datetime: str | None = None
    af_add_date: str | None = None