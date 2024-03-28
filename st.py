import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data
unique_users = 60735
total_posts = 2540207
total_likes = 30597519
nsfw_posts = 1626131
nsfw_likes = 10943083
avg_likes_per_post = 12.05
date_most_posts = "2024-01-14"
avg_posts_per_day = 4704.09
likes_percentile = [3, 9, 50]

# Top 100 users data
top_users_data = {'profile_name': ['Yevhen S.', 'Rukia Best Girl', 'Zero zero', 'Burger', 'Naked Ninja', 'b4ai', 'Vi - Vi', 'Dario', 'Catspaws', 'idiotcornball', 'Some Display Name', 'AManApart', 'Teemuu', 'Dreamer', 'Ananda', 'Alan Smithee', 'Magic Studio', 'Versus Z', 'AI MVP', 'GLM2022', 'ronny schipper', 'Maō of Saints', 'Lucifur Bunny', '🦘 dancematd an 🦘', 'wyingjing',
 'Puf', 'Bettie Blasphemy', '', 'somethin', 'yuun', 'blafba', 'Raz', '🤜⚡🤛', 'Dio', 'Elfboi', 'Strikai', 'Joe Momma', 'Ryo', '🔥Ph Hub🔥', 'MC Outlaw (MC Outlaw)', 'AIA', 'Tiago SG', 'Mythos', 'John Silver', '✷', 'Sloppy Joe', 'fortis', 'Megumin', 'BERCOS', 'Dirty', 'DesDc', 'Gimonya', 'Tits and Ass', 'Leonardo Mafra Reina', 'WhyNot Raisins', 'rain', 'Bocah Tua', 'Julia Rubymoon', 'Khutulun', 'muffin zetta', 'Willow', 'Lauriel 🌺', 'EMMANUEL Dacosta', 'Vivio Kaiser', 'Hello 👋 Hello', 'Azusa is cute from birth', 'R', 'Pain&sin', 'D Do', 'Misaki Akeno', 'Bignemo90', 'Hentai Art Ai', 'Mår', 'Alan Hovis', 'Grimaldus', 'ninci (new account)', 'อสูรในสายหมอก', '🟡', 'Abhimanyu', 'Aki', 'SomaC Sel ah. T v2.0 ᴾᵉᵒᵖˡᵉᵃʳᵉˢʰⁱᵗ', '[V]', 'Damien S', 'Izumi Kanto', 'Tsuna', 'veni_vidi_vici_m', 'YoursToPlay', 'Zio', 'Zero', 'Ian Bezziemi', 'JenaUrf', 'Edona', 'Jay Dee', 'Ententom', 'Sin_Scarlet', 'Atti', 'semoxtv', 'ry juice', 'Yugio', 'MAXAM'], 'user_uuid': ['8a33a752-0d4d-4304-9baa-e954db49a159', '5e32cee2-9697-4af7-9fc6-8d7221ba37b9', '1fadcdf9-b0b5-4c53-b272-adc5ad50a61d', '518bffed-0793-43d8-a1a2-ed2ef66550ec', '707af4bc-6590-42ac-ab56-a30b14195b3e', '492c6710-84f8-4d25-8173-4637745bbb40', '6da49b5d-7c5d-4019-a21e-611c879269d3', '13f28181-c510-4b59-8252-250447cdba81', '737af57f-a026-4725-a1f3-fd9577491f8a', '7b8e78ad-2ceb-4f23-a2be-cd4eabb3b708', 'aeeff653-daa4-4f5f-ad72-2ade8496766b', '473fa9e5-35ac-4112-9156-b49ee8224276', 'b9aae266-d509-42e5-be2b-d09195a35756', '8cca3300-6be2-4cf9-a9f9-04871d32ed44', 'c236b7a2-69d5-49fc-ad2d-0281a0e5b29c', 'd4be5799-1c43-4420-a3b2-2697eb99429f', '34b41b77-c345-4c5d-9518-71a09bfda8e5', '09c122e8-51e7-4578-9cfc-351e15ff6bdf', '07168cd3-f5ae-4b81-8171-dbb411b715e0', '842a45e6-edff-47b1-a379-74a931ffa2a0', '1c4580b2-6145-40a5-924f-4faec29971a7', 'f194e0cd-1d7f-4d4b-bd33-dd3f4d910c80', 'b6536b6a-31fa-4c67-a96b-be97b3e726e0', 'e1e9c0c0-cbe3-4d6d-b07a-d0feae1a7cd8', '8915f501-1fea-4f0b-bf48-b32ef27443c9', 'ddae3b36-f3ec-4ee0-8d53-91cd579bc760', '6c9eb40c-a451-4c73-b364-9103e1b8819e', '58104f03-f2b7-42bb-a3aa-2e9a55838bc2', '0222d673-0a40-4e58-aaea-c9b3cc36f0e4', 'e4829ffb-7420-4f49-bb03-0332bcd69cdb', 'e68633ad-2086-40f2-9b02-d7e5a041b169', 'a8f98b54-0677-4bc4-bd74-ac68fe234116', 'bbbdf4b5-81e3-488d-abda-ac58e7cf1b56', 'eedf979c-10f9-4562-b2f9-93bd79db1428', '6fb420ba-ecbf-487a-a9c6-a4afeb8f6659', 'f90baa87-a5c8-4db1-a22e-398296313043', '14fed926-805c-4429-ac34-ba93b5242ce3', '82648d4e-c847-4a82-9670-41e758622721', '60f5ab4c-8b3a-4bc8-94ae-64f653a09e26', '1c4b5bdf-2bcc-4b9e-83cd-efa0e6ed2019', 'eb1900d9-c6ea-42a7-aaa1-09108ecfc15b', 'f5f0b1b6-a90a-417c-b9aa-9dc57ed2482d', '96bb7db3-0750-486b-9510-50a1a450a6a0', 'b47bc1ab-bdc3-4397-9aad-e1516f5691f8', '67077fb7-6267-4ca2-bb45-95ff15cf3189', '5f22910b-8734-4759-bddd-b75f0706b4f3', '38241e5d-5d73-49f2-accc-d67ed6b8956d', '5b1acaa1-26fe-4664-ac3d-d0f181aaa933', '9dc191d5-c4ee-474f-9776-0634d0b59efb', '7a183bb5-7941-49eb-a42c-73bb1423253e', '514f5e11-ddd1-4268-986d-c9b124223756', 'cd8d8ed7-864d-4b92-abe5-c1ea60e7276b', 'e5a7fe40-1528-4561-9d35-76fdf20f736b', 'c19f174f-ef6f-481b-b7a3-ccbf92acb5c8', '9382d75a-2bd9-45c5-be04-0829d60af145', '4ed5472a-df3e-476e-beff-5f40c23ec54b', '49ef0992-1427-409a-9a06-f355370f7673', '7f1d07ed-3e83-42c3-9bc4-94658595b7a5', '89d74016-38b0-46e1-86db-2a71b0780d08', 'e7dce258-5b84-4c04-8653-bd5b3d7474d6', 'e356be6c-e598-46ae-a136-78eeca5d81e7', '06fce36d-1910-4fb4-aa7e-807c10715961', '93572140-b85b-42b0-9f71-b739dbbcc734', 'be6cb0c1-5ebe-4cd8-8422-d9d35740ec7b', '24646f3c-0deb-4446-a91d-d6a283c60e42', 'd5cd8d57-9f6d-498f-84ac-21dbe1a60688', 'a2e0f01a-62ae-469e-8a2f-eef4eddc3516', 'f0e1c6fd-2acb-4a86-be74-1678bf4911be', '681d2fa1-30e9-4844-833a-52001bb3587a', '44979c02-5e45-4f96-95b2-111e379b4756', 'cc76f5c2-74ad-4103-9365-55ce05987270', '6a353ffd-bd77-4684-b053-237971a21d8b', '6bff2b87-735d-40f1-8201-0ac207ce8c74', '7b83bd40-f77b-4d32-afc2-b4ea2d6832c6', '648ccb71-fb09-45c7-9778-35441b53482f', 'b379150c-e275-43f1-914c-4c795b1b4f58', 'c32c9ba6-15f8-466e-bd08-d367ef50a0cd', 'c0f5ba69-c699-40f7-bb3c-b478c7bd2671', '20047062-e3b5-4848-8078-6a8f728e731f', '63e1e5d8-5158-4da9-a1a3-2eb94bc03f9b', '7a274a0a-b67b-4de8-9953-203576e25a7f', '31e15480-43d6-4b4c-b960-d81f97791bd5', '49e4ddc1-19f8-4d97-bd46-ff6db1f51eca', '73bc8052-e36a-4809-baac-4773dfdab614', '7d507973-411e-4014-908e-ca616392f919', 'a9bee5f0-44ed-46b8-b59e-76ff14e14c1f', '68af5e56-e179-4140-babb-68637d4f2908', '6567562d-b83a-4799-bcfd-f774045f58c4', '157b4840-10da-475a-a6e6-6a09382a2229', 'bb3eaff9-8770-4996-bdf8-a0004f925c6e', '7c6a73f5-d7ce-4900-b53c-96507502c7b1', 'c73d7632-7e9f-4a1a-a478-b040b2753f09', '824c619f-b11d-4a94-a59f-d5d1c32eede2', 'd9fdb886-349a-4f9a-b9e5-faedfbbf67b6', 'e00d56fd-da8a-45a5-86fd-980574a056b3', '204f3ee2-47b8-42a2-b62c-b767dc6f59fa', 'c715a317-e9e1-4a55-8c5c-0915c67273e9', '62cfc41d-948a-4bb6-b4be-3c4557e4897f', '3f50fbb0-5e05-48f1-a889-dcc7d2807ce3', '0ce1d264-d764-40ab-aeda-3ec2e9b616c1'], 'post_count': [30084, 23919, 15396, 14655, 13304, 10624, 9274, 9132, 8407, 8329, 8236, 7244, 7121, 6675, 6662, 6638, 6322, 6223, 6037, 6008, 5879, 5673, 5395, 5315, 5250, 5212, 4998, 4972, 4857, 4841, 4814, 4764, 4756, 4703, 4529, 4432, 4255, 4248, 4083, 4071, 4024, 3975, 3880, 3851, 3809, 3750, 3736, 3736, 3664, 3635, 3577, 3564, 3511, 3497, 3394, 3379, 3365, 3314, 3250, 3245, 3230, 3182, 3162, 3113, 3072, 3046, 3040, 3025, 3010, 2977, 2947, 2896, 2883, 2873, 2850, 2836, 2836, 2824, 2822, 2816, 2807, 2796, 2784, 2763, 2746, 2724, 2722, 2703, 2699, 2669, 2662, 2660, 2639, 2637, 2613, 2608, 2582, 2581, 2578, 2569]}
top_users_df = pd.DataFrame(top_users_data)

top_users_likes = {'profile_name': ['Zero zero', 'Amaiko Ayakashi', 'Teemuu', '🔥Ph Hub🔥', 'Hello 👋 Hello', 'Maō of Saints', 'ry juice', 'Puf', 'timbles', 'Elara the Mage 🪄', 'Izumi Kanto', 'scoot🛵', 'HeisMad', 'Julia Rubymoon', 'wyin gjing', '🦒Giraffe Boi Danny🦒', 'Bocah Tua', 'Rukia Best Girl', 'veni_vidi_vici_m', 'Mirror', 'Wolf (El Wolfo)', 'Grimaldus', 'Siddorf', 'Vex 🐇', 'NSFW Paradise', 'ninci (new account)', 'PPX', 'Ij', 'ry k', 'EvaClausAI', 'still dope', 'Yevhen S.', '[V]', 'Autumn', 'Misaki Akeno', 'Milunya Essence', '🦘 dancematdan 🦘', 'Brad', 'Prime', 'Amish', 'Ecchiman',   'Remilia', 'The Cute in Yellow', '🐐Lucifer🐐', 'rain', 'Zero<(=⩊=)>', 'Aki', 'Speedlife', 'Temperance', '✨Hexy✨', 'Lilianna', 'Natchu', 'Katnip', 'six', 'Takuu', '𝓜𝓪𝓽𝓱𝓮𝔀 𝓒 - 𝓣𝓲𝓶𝓮 𝓦𝓲𝔃𝓪𝓻𝓭🧙\u200d♂️', 'Risu', 'Leonardo Mafra                  Reina', 'Ryo', 'Rae 屈愛', 'Naked Ninja', 'Stregal', 'Some Display Name', 'Gerson D. Rider', 'Willow', 'Senlin', '1818 🌟 [SDガール]', '', 'Nini', 'Degrees of difference', 'Through the fire', 'LauLau', 'Burgahr', 'Iroha', 'AKIRA', 'Langaku', 'Call_Me_Toni', 'Ananda', 'shadow0667', 'Tired Puppy', 'Catspaws', 'Tivadar', '-FreaknesS-', 'Alicia', 'Akiyoshi', 'Sigurd', 'Kirbynator', 'Bettie Blasphemy', 'BERCOS', 'Phlyer', '🎸☯️ Yinyin ☯️🎸', 'semoxtv', '\u200c', 'Zablinski', '𝔸� 𝕥𝕚𝕤𝕥𝕚𝕔  𝕤𝕡𝕖
𝕔𝕥𝕒𝕥𝕠𝕣', 'Jordan_M', 'Dario', \'\\', 'Majin de Géminis', 'Noxi'], 'user_uuid': ['1fadcdf9-b0b5-4c      53-b272-adc5ad50a61d', '0fee7fab-9ca0-484e-9994-eb5e04ceb8f5', 'b9aae266-d509-42e5-be2b-d09195a35756', '60f5ab4c-8b3a-4bc8-94ae-64f653a09e26', '24646f3c-0deb-4446-a91d-d6a283c60e42', 'f194e0cd-1d7f-4d4b-bd33-dd3f4d910c80', '62cfc41d-948a-4bb6-b4be-3c4557e4897f', 'ddae3b36-f3ec-4ee0-8d53-91cd579bc760', 'ee6e0470-2144-4648-83d1-f64e8ab3a801', 'a06f278b-7781-43a4-87cb-5354925afa96', '73bc8052-e36a-4809-baac-4773dfdab614', 'c0a8be3c-cadd-437d-9624-97f80635b354', 'dddde05a-172e-41cf-a07a-269f9f0cf1a7', '7f1d07ed-3e83-42c3-9bc4-94658595b7a5', '8915f501-1fea-4f0b-bf48-b32ef27443c9', '531e6a5e-9be6-473e-aa7b-2f49ccb80146', '49ef0992-1427-409a-9a06-f355370f7673', '5e32cee2-9697-4af7-9fc6-8d7221ba37b9', 'a9bee5f0-44ed-46b8-b59e-76ff14e14c1f', 'a8deac57-4ac6-4115-afc5-c5fe434623a1', '79136320-5864-47ea-827b-6d25a279bbd1', '648ccb71-fb09-45c7-9778-35441b53482f', '9d163c8e-51c9-47c2-a488-fe49004d00ae', '2788f315-7f17-487a-b26c-64cb09c001f2', '26bcb655-f436-4b0e-8414-62e0aea8b0e7', 'b379150c-e275-43f1-914c-4c795b1b4f58', '0833625b-ea56-4b2e-a8a7-64abea9bf1a2', '35dd6225-0a2f-4872-b9da-256cd1cf8b34', '9110105a-1c2b-4527-8cdd-63abdba9a7b0', '7e243e76-3d9f-4b09-8926-a5698cc87011', 'd603d665-89ff-4d79-aa69-11172abb9f50', '8a33a752-0d4d-4304-9baa-e954db49a159', '31e15480-43d6-4b4c-b960-d81f97791bd5', 'ed88199e-ee45-4636-bea5-266614ca62ba', '44979c02-5e45-4f96-95b2-111e379b4756', '11f63b9e-7349-411b-b518-3ebd3324bab3', 'e1e9c0c0-cbe3-4d6d-b07a-d0feae1a7cd8', 'b23d146a-89e2-4f36-9a3c-b714b766423c', '3f13ac7d-0798-4ae8-8b56-1e06ab0cba36', '7d7c2b75-b0f3-480f-af58-0059c43b6f88', 'c811e82d-0612-4e6f-9805-a8b3dfe4afd3', '8a2119bc-6e1b-49c5-a1e0-d62c01497a07', '15db6cd2-8ff7-42f1-917f-b43c203f675b', '5fa14a22-43bf-499a-9f0f-2b34a8d23576', '4ed5472a-df3e-476e-beff-5f40c23ec54b', '9ca45e8e-7981-4539-bbab-86310eeb88a1', '63e1e5d8-5158-4da9-a1a3-2eb94bc03f9b', '0f6da447-6a28-4af0-8e62-897c6f66953c', 'e4a3f042-0c35-40c1-95c9-7497b86bbb87', '7b3676aa-ef73-4205-a698-820a2d658a44', '229f6660-c66b-459a-842b-a944577f51cf', '663af217-0b4a-40fd-a51f-394191ec2bec', '609c9c02-96bf-4e8d-a7cd-44b3a8a88ae9', 'ae584f4e-55c5-4977-aab0-8d3c5b5d52ad', '96bc934f-eb26-4909-8208-5a7ffe99ac21', '2e2712b0-1b44-4c4c-bd48-59f6a2ff4f28', 'e0a8dc0d-24b2-427e-b1ed-87bdf136b9ac', 'c19f174f-ef6f-481b-b7a3-ccbf92acb5c8', '82648d4e-c847-4a82-9670-41e758622721', '4785a75b-aa47-4bef-9dc9-4edc8f19f2b3', '707af4bc-6590-42ac-ab56-a30b14195b3e', '2ce5a235-3b49-4d19-94cc-82a51f608bef', 'aeeff653-daa4-4f5f-ad72-2ade8496766b', '0f48626a-893a-4906-97bc-e3122f2474e9', 'e356be6c-e598-46ae-a136-78eeca5d81e7', 'b0c03c3e-e566-4ac5-916b-21db43d56ba0', '4da3968c-9bf4-47f9-93c7-343262a5638a', 'b5cbaff5-2601-4a10-89a5-f5a269fe42ae', '24d7061e-acd0-4b68-a0ab-13f235c5593e', '2811f638-4e0a-4fb6-8b54-843402da01d0', '25a64ac5-14d3-4f69-8284-4c123048f2bc', '3f288873-8b0f-412c-a56a-d469c43fee73', '6f1a492e-dd1b-400e-b11b-2cbd7d16dd47', '5fd9967b-d576-498a-8fc4-b508e30423e3', '231e8ae4-4561-400e-b1f7-9ba1b40230b2', '7426396e-5f91-4fd0-89b3-4a043c004ac4', 'a31501cd-c646-4d2f-9576-93512f0bfe5c', 'c236b7a2-69d5-49fc-ad2d-0281a0e5b29c', '7d92174f-b616-4688-a2b1-aea1c05aa301', '4b5df674-9db1-44b5-b997-4feb6ce60865', '737af57f-a026-4725-a1f3-fd9577491f8a', '83c5ff95-2589-471d-ab40-cb600f3a8772', 'feff31d9-af0e-4fa0-b3e0-f4a4767d983e', '7ada8088-4be5-425d-804d-303c27b97821', '4a931d9e-1fdb-493a-abf8-1502f7d2bf13', '25d4b36f-8268-4c52-8a91-58247484eb20', '05a5e6d1-6032-4e2a-8477-0f050548aa35', '6c9eb40c-a451-4c73-b364-9103e1b8819e', '9dc191d5-c4ee-474f-9776-0634d0b59efb', '6c3b8bdb-1e6e-455e-8841-d6c79139b4fd', '338f158e-d839-4dd6-9fca-f8e2cfcecec4', 'c715a317-e9e1-4a55-8c5c-0915c67273e9', 'fe2b24f8-9086-4dff-ae87-f7e02dabf555', 'a0665e8c-167c-4d37-a45f-37bf4a5dc663', 'c3744dec-e334-4a10-8917-be3edf5baacc', 'a511fc91-6e8b-41a5-bfff-245d3a08b252', '13f28181-c510-4b59-8252-250447cdba81', '58104f03-f2b7-42bb-a3aa-2e9a55838bc2', 'bf9b05cf-f9fb-40c0-9de4-3eab88f7e052', 'b4c3530c-2bf4-4936-a2cf-53ddd1e767eb'], 'likes_count': [456997, 427268, 270952, 253993, 243648, 229908, 226800, 197927, 197865, 194463, 190725, 183104, 180058, 175794, 162692, 162142, 157158, 153354, 152690, 142600, 139269, 136590, 136100, 135462, 134980, 131850, 121453, 116320, 114606, 111705, 106505, 106476, 103586, 98248, 97536, 94676, 92281, 91390, 89999, 87231, 86214, 86167, 84746, 83707, 83141, 82089, 81926, 79175, 78275, 78050, 77678, 77119, 76777, 76416, 76152, 74353, 72581, 70812, 70418, 69786, 69083, 68414, 68333, 67688, 66388, 65795, 65158, 63706, 63436, 63400, 63268, 63150, 62794, 62389, 61795, 61112, 60475, 57905, 57491, 57009, 56992, 56286, 55563, 55496, 55091, 54927, 54844, 54789, 54360, 53980, 53967, 53726, 52902, 52652, 52487, 52486, 51840, 50556, 50101, 49502]}
top_users_likes_df = pd.DataFrame(top_users_data)

# Posts by day data
posts_by_day_data = {
    "date": ["2023-08-09", "2023-08-10", "2023-08-11"],  # Add more dates here
    "total_posts": [3426, 4600, 5349],  # Add more total posts here
    "nsfw_posts": [1934, 2743, 3199],  # Add more nsfw posts here
    "nsfw_percentage": [56.450671, 59.630435, 59.805571]  # Add more nsfw percentage here
}
posts_by_day_df = pd.DataFrame(posts_by_day_data)

# Posts by hour data
posts_by_hour_data = {
    "Hour": list(range(24)),
    "Post Count": [87555, 90077, 83852, 78812, 77059, 72662, 71416, 67774, 65058, 59996, 63106, 66863, 68479, 73217, 79746, 83824, 85581, 84407, 82931, 83693, 82518, 79105, 76382, 74387]
}
posts_by_hour_df = pd.DataFrame(posts_by_hour_data)

# Sidebar
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", ["Overview", "Top Users", "Posts by Day", "Posts by Hour"])

# Page content
st.title("YDStat")

if selected_page == "Overview":
    st.write(f"Unique Users: {unique_users}")
    st.write(f"Total Posts: {total_posts}")
    st.write(f"Total Likes: {total_likes}")
    st.write(f"NSFW Posts: {nsfw_posts} ({(nsfw_posts / total_posts) * 100:.2f}%)")
    st.write(f"NSFW Likes: {nsfw_likes} ({(nsfw_likes / total_likes) * 100:.2f}%)")
    st.write(f"Average Likes per Post: {avg_likes_per_post}")
    st.write(f"Date with Most Posts: {date_most_posts}")
    st.write(f"Average Posts per Day: {avg_posts_per_day}")
    st.write(f"Likes by Percentile: {likes_percentile}")

elif selected_page == "Top Users":
    st.subheader("Top 100 Users by Number of Posts")
    st.dataframe(top_users_df)
    st.subheader("Top 100 Users by Number of Likes")
    st.dataframe(top_users_likes_df)

elif selected_page == "Posts by Day":
    st.subheader("Posts by Day")
    st.line_chart(posts_by_day_df.set_index("date")[["total_posts", "nsfw_posts"]])

elif selected_page == "Posts by Hour":
    st.subheader("Posts by Hour")
    st.bar_chart(posts_by_hour_df.set_index("Hour"))
