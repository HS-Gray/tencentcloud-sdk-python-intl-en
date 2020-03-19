# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class AlgorithmInfo(AbstractModel):
    """Algorithm name and ID

    """

    def __init__(self):
        """
        :param KeyUsage: Algorithm ID
        :type KeyUsage: str
        :param Algorithm: Algorithm name
        :type Algorithm: str
        """
        self.KeyUsage = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyUsage = params.get("KeyUsage")
        self.Algorithm = params.get("Algorithm")


class AsymmetricRsaDecryptRequest(AbstractModel):
    """AsymmetricRsaDecrypt request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`
        :type Ciphertext: str
        :param Algorithm: Corresponding algorithm when a public key is used for encryption. Valid values: RSAES_PKCS1_V1_5, RSAES_OAEP_SHA_1, RSAES_OAEP_SHA_256
        :type Algorithm: str
        """
        self.KeyId = None
        self.Ciphertext = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")
        self.Algorithm = params.get("Algorithm")


class AsymmetricRsaDecryptResponse(AbstractModel):
    """AsymmetricRsaDecrypt response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Plaintext: Base64-encoded plaintext after decryption
        :type Plaintext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class AsymmetricSm2DecryptRequest(AbstractModel):
    """AsymmetricSm2Decrypt request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`, whose length cannot exceed 256 bytes.
        :type Ciphertext: str
        """
        self.KeyId = None
        self.Ciphertext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")


class AsymmetricSm2DecryptResponse(AbstractModel):
    """AsymmetricSm2Decrypt response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Plaintext: Base64-encoded plaintext after decryption
        :type Plaintext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class CancelKeyDeletionRequest(AbstractModel):
    """CancelKeyDeletion request structure.

    """


class CancelKeyDeletionResponse(AbstractModel):
    """CancelKeyDeletion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateKeyRequest(AbstractModel):
    """CreateKey request structure.

    """

    def __init__(self):
        """
        :param Alias: Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1–60 letters, digits, `-`, and `_`, and must begin with a letter or digit. The `kms-` prefix is used for Tencent Cloud products.
        :type Alias: str
        :param Description: 
        :type Description: str
        :param KeyUsage: Key purpose. The default value is `ENCRYPT_DECRYPT` (creating a symmetric key for encryption and decryption). Other valid values include `ASYMMETRIC_DECRYPT_RSA_2048` (creating an RSA2048 asymmetric key for encryption and decryption) and `ASYMMETRIC_DECRYPT_SM2` (creating an SM2 asymmetric key for encryption and decryption).
        :type KeyUsage: str
        :param Type: Specifies the key type. Default value: 1. Valid value: 1 - default type, indicating that the CMK is created by KMS; 2 - EXTERNAL type, indicating that you need to import key material. For more information, please see the `GetParametersForImport` and `ImportKeyMaterial` API documents.
        :type Type: int
        """
        self.Alias = None
        self.Description = None
        self.KeyUsage = None
        self.Type = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")


class CreateKeyResponse(AbstractModel):
    """CreateKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DecryptRequest(AbstractModel):
    """Decrypt request structure.

    """

    def __init__(self):
        """
        :param CiphertextBlob: The ciphertext data to be decrypted.
        :type CiphertextBlob: str
        :param EncryptionContext: 
        :type EncryptionContext: str
        """
        self.CiphertextBlob = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.EncryptionContext = params.get("EncryptionContext")


class DecryptResponse(AbstractModel):
    """Decrypt response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImportedKeyMaterialRequest(AbstractModel):
    """DeleteImportedKeyMaterial request structure.

    """

    def __init__(self):
        """
        :param KeyId: Specifies the EXTERNAL CMK for which to delete the key material.
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DeleteImportedKeyMaterialResponse(AbstractModel):
    """DeleteImportedKeyMaterial response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DescribeKeyResponse(AbstractModel):
    """DescribeKey response structure.

    """

    def __init__(self):
        """
        :param KeyMetadata: Key attribute information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadata: :class:`tencentcloud.kms.v20190118.models.KeyMetadata`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadata") is not None:
            self.KeyMetadata = KeyMetadata()
            self.KeyMetadata._deserialize(params.get("KeyMetadata"))
        self.RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys request structure.

    """

    def __init__(self):
        """
        :param KeyIds: List of IDs of the CMKs to be queried in batches. Up to 100 `KeyId` values are supported in one query.
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys response structure.

    """

    def __init__(self):
        """
        :param KeyMetadatas: List of returned attribute information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class DisableKeyRequest(AbstractModel):
    """DisableKey request structure.

    """


class DisableKeyResponse(AbstractModel):
    """DisableKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation request structure.

    """


class DisableKeyRotationResponse(AbstractModel):
    """DisableKeyRotation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys request structure.

    """


class DisableKeysResponse(AbstractModel):
    """DisableKeys response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey request structure.

    """


class EnableKeyResponse(AbstractModel):
    """EnableKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation request structure.

    """


class EnableKeyRotationResponse(AbstractModel):
    """EnableKeyRotation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys request structure.

    """


class EnableKeysResponse(AbstractModel):
    """EnableKeys response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncryptRequest(AbstractModel):
    """Encrypt request structure.

    """


class EncryptResponse(AbstractModel):
    """Encrypt response structure.

    """

    def __init__(self):
        """
        :param CiphertextBlob: Base64-encoded encrypted ciphertext
        :type CiphertextBlob: str
        :param KeyId: 
        :type KeyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CiphertextBlob = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class GenerateDataKeyRequest(AbstractModel):
    """GenerateDataKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: 
        :type KeyId: str
        :param KeySpec: Specifies the encryption algorithm and size of the `DataKey`. Valid values: AES_128, AES_256. Either `KeySpec` or `NumberOfBytes` must be specified.
        :type KeySpec: str
        :param NumberOfBytes: Length of the `DataKey`. If both `NumberOfBytes` and `KeySpec` are specified, `NumberOfBytes` will prevail. Minimum value: 1; maximum value: 1024. Either `KeySpec` or `NumberOfBytes` must be specified.
        :type NumberOfBytes: int
        :param EncryptionContext: 
        :type EncryptionContext: str
        """
        self.KeyId = None
        self.KeySpec = None
        self.NumberOfBytes = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeySpec = params.get("KeySpec")
        self.NumberOfBytes = params.get("NumberOfBytes")
        self.EncryptionContext = params.get("EncryptionContext")


class GenerateDataKeyResponse(AbstractModel):
    """GenerateDataKey response structure.

    """

    def __init__(self):
        """
        :param KeyId: 
        :type KeyId: str
        :param Plaintext: 
        :type Plaintext: str
        :param CiphertextBlob: Base64-encoded ciphertext that is encrypted by `DataKey`. You should keep the ciphertext private.
        :type CiphertextBlob: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.CiphertextBlob = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.RequestId = params.get("RequestId")


class GenerateRandomRequest(AbstractModel):
    """GenerateRandom request structure.

    """

    def __init__(self):
        """
        :param NumberOfBytes: Length of the random number. Minimum value: 1. Maximum value: 1024
        :type NumberOfBytes: int
        """
        self.NumberOfBytes = None


    def _deserialize(self, params):
        self.NumberOfBytes = params.get("NumberOfBytes")


class GenerateRandomResponse(AbstractModel):
    """GenerateRandom response structure.

    """

    def __init__(self):
        """
        :param Plaintext: Base64-encoded plaintext of the randomly generated number. You need to Base64-decode it to get the plaintext.
        :type Plaintext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus request structure.

    """


class GetKeyRotationStatusResponse(AbstractModel):
    """GetKeyRotationStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetParametersForImportRequest(AbstractModel):
    """GetParametersForImport request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique ID of a CMK. The CMK for which to get the key parameters must be of the `EXTERNAL` type, i.e., Type = 2 when the CMK is created by the `CreateKey` API.
        :type KeyId: str
        :param WrappingAlgorithm: Specifies the algorithm for key material encryption. Currently, `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1`, and `RSAES_OAEP_SHA_256` are supported.
        :type WrappingAlgorithm: str
        :param WrappingKeySpec: Specifies the type of wrapping key. Currently, only `RSA_2048` is supported.
        :type WrappingKeySpec: str
        """
        self.KeyId = None
        self.WrappingAlgorithm = None
        self.WrappingKeySpec = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.WrappingAlgorithm = params.get("WrappingAlgorithm")
        self.WrappingKeySpec = params.get("WrappingKeySpec")


class GetParametersForImportResponse(AbstractModel):
    """GetParametersForImport response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique ID of a CMK, which is used to specify the CMK into which to import key material.
        :type KeyId: str
        :param ImportToken: The token required for importing key material, which is used as a parameter for `ImportKeyMaterial`.
        :type ImportToken: str
        :param PublicKey: The Base64-encoded RSA public key used to encrypt key material before importing it with `ImportKeyMaterial`.
        :type PublicKey: str
        :param ParametersValidTo: Validity period of the token and public key. A token and public key can only be imported when they are valid. If they are expired, you will need to call the `GetParametersForImport` API again to get a new token and public key.
        :type ParametersValidTo: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.ImportToken = None
        self.PublicKey = None
        self.ParametersValidTo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ImportToken = params.get("ImportToken")
        self.PublicKey = params.get("PublicKey")
        self.ParametersValidTo = params.get("ParametersValidTo")
        self.RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID.
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID.
        :type KeyId: str
        :param PublicKey: Base64-encoded public key content.
        :type PublicKey: str
        :param PublicKeyPem: Public key content in PEM format.
        :type PublicKeyPem: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.PublicKey = None
        self.PublicKeyPem = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PublicKey = params.get("PublicKey")
        self.PublicKeyPem = params.get("PublicKeyPem")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus request structure.

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImportKeyMaterialRequest(AbstractModel):
    """ImportKeyMaterial request structure.

    """

    def __init__(self):
        """
        :param EncryptedKeyMaterial: Base64-encoded key material that encrypted with the `PublicKey` returned by `GetParametersForImport`. For the KMS of SM-CRYPTO version, the length of the key material should be 128 bits, while for KMS of FIPS-compliant version, the length should be 256 bits.
        :type EncryptedKeyMaterial: str
        :param ImportToken: Import token obtained by calling `GetParametersForImport`.
        :type ImportToken: str
        :param KeyId: Specifies the CMK into which to import key material, which must be the same as the one specified by `GetParametersForImport`.
        :type KeyId: str
        :param ValidTo: Unix timestamp of the key material’s expiration time. If this value is empty or 0, the key material will never expire. To specify the expiration time, it should be later than the current time. Maximum value: 2147443200.
        :type ValidTo: int
        """
        self.EncryptedKeyMaterial = None
        self.ImportToken = None
        self.KeyId = None
        self.ValidTo = None


    def _deserialize(self, params):
        self.EncryptedKeyMaterial = params.get("EncryptedKeyMaterial")
        self.ImportToken = params.get("ImportToken")
        self.KeyId = params.get("KeyId")
        self.ValidTo = params.get("ValidTo")


class ImportKeyMaterialResponse(AbstractModel):
    """ImportKeyMaterial response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class KeyMetadata(AbstractModel):
    """CMK属性信息

    """

    def __init__(self):
        """
        :param KeyId: 
        :type KeyId: str
        :param Alias: 
        :type Alias: str
        :param CreateTime: 
        :type CreateTime: int
        :param Description: 
        :type Description: str
        :param KeyState: CMK status. Valid values: Enabled, Disabled, PendingDelete, PendingImport.
        :type KeyState: str
        :param KeyUsage: CMK purpose. Valid values: ENCRYPT_DECRYPT, ASYMMETRIC_DECRYPT_RSA_2048, ASYMMETRIC_DECRYPT_SM2
        :type KeyUsage: str
        :param Type: CMK type. 2: FIPS-compliant; 4: SM-CRYPTO
        :type Type: int
        :param CreatorUin: 
        :type CreatorUin: int
        :param KeyRotationEnabled: 
        :type KeyRotationEnabled: bool
        :param Owner: 
        :type Owner: str
        :param NextRotateTime: 
        :type NextRotateTime: int
        :param DeletionDate: 
        :type DeletionDate: int
        :param Origin: CMK key material type. TENCENT_KMS: created by KMS; EXTERNAL: imported by user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: str
        :param ValidTo: It’s valid when `Origin` is `EXTERNAL`, indicating the expiration date of key material. 0 means valid forever.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidTo: int
        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.Type = None
        self.CreatorUin = None
        self.KeyRotationEnabled = None
        self.Owner = None
        self.NextRotateTime = None
        self.DeletionDate = None
        self.Origin = None
        self.ValidTo = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")
        self.CreatorUin = params.get("CreatorUin")
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.Owner = params.get("Owner")
        self.NextRotateTime = params.get("NextRotateTime")
        self.DeletionDate = params.get("DeletionDate")
        self.Origin = params.get("Origin")
        self.ValidTo = params.get("ValidTo")


class ListAlgorithmsRequest(AbstractModel):
    """ListAlgorithms request structure.

    """


class ListAlgorithmsResponse(AbstractModel):
    """ListAlgorithms response structure.

    """

    def __init__(self):
        """
        :param SymmetricAlgorithms: Symmetric encryption algorithms supported in this region
        :type SymmetricAlgorithms: list of AlgorithmInfo
        :param AsymmetricAlgorithms: Asymmetric encryption algorithms supported in this region
        :type AsymmetricAlgorithms: list of AlgorithmInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SymmetricAlgorithms = None
        self.AsymmetricAlgorithms = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SymmetricAlgorithms") is not None:
            self.SymmetricAlgorithms = []
            for item in params.get("SymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.SymmetricAlgorithms.append(obj)
        if params.get("AsymmetricAlgorithms") is not None:
            self.AsymmetricAlgorithms = []
            for item in params.get("AsymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.AsymmetricAlgorithms.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail request structure.

    """

    def __init__(self):
        """
        :param Offset: 
        :type Offset: int
        :param Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200.
        :type Limit: int
        :param Role: 
        :type Role: int
        :param OrderType: 
        :type OrderType: int
        :param KeyState: Filters by CMK status. 0: all CMKs; 1: CMKs in `Enabled` status only; 2: CMKs in `Disabled` status only; 3: CMKs in `PendingDelete` status only (i.e., keys with schedule deletion enabled); 4: CMKs in `PendingImport` status only.
        :type KeyState: int
        :param SearchKeyAlias: 
        :type SearchKeyAlias: str
        :param Origin: Filters by CMK type. "TENCENT_KMS" indicates to filter CMKs whose key materials are created by KMS; "EXTERNAL" indicates to filter CMKs of `EXTERNAL` type whose key materials are imported by users; "ALL" or empty indicates to filter CMKs of both types. This value is case-sensitive.
        :type Origin: str
        :param KeyUsage: Filter by `KeyUsage` of CMKs. If this parameter is left empty, it means to filter all CMKs. Valid values: ENCRYPT_DECRYPT, ASYMMETRIC_DECRYPT_RSA_2048, ASYMMETRIC_DECRYPT_SM2
        :type KeyUsage: str
        """
        self.Offset = None
        self.Limit = None
        self.Role = None
        self.OrderType = None
        self.KeyState = None
        self.SearchKeyAlias = None
        self.Origin = None
        self.KeyUsage = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        self.OrderType = params.get("OrderType")
        self.KeyState = params.get("KeyState")
        self.SearchKeyAlias = params.get("SearchKeyAlias")
        self.Origin = params.get("Origin")
        self.KeyUsage = params.get("KeyUsage")


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: 
        :type TotalCount: int
        :param KeyMetadatas: List of returned attribute information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeysRequest(AbstractModel):
    """ListKeys request structure.

    """


class ListKeysResponse(AbstractModel):
    """ListKeys response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReEncryptRequest(AbstractModel):
    """ReEncrypt request structure.

    """


class ReEncryptResponse(AbstractModel):
    """ReEncrypt response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ScheduleKeyDeletionRequest(AbstractModel):
    """ScheduleKeyDeletion request structure.

    """


class ScheduleKeyDeletionResponse(AbstractModel):
    """ScheduleKeyDeletion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias request structure.

    """


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription request structure.

    """

    def __init__(self):
        """
        :param Description: 
        :type Description: str
        :param KeyId: ID of the CMK for which to modify the description
        :type KeyId: str
        """
        self.Description = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.KeyId = params.get("KeyId")


class UpdateKeyDescriptionResponse(AbstractModel):
    """UpdateKeyDescription response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")