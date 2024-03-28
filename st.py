import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

# Data
unique_users = 60735
total_posts = 2540207
total_likes = 30597519
nsfw_posts = 1626131
avg_likes_per_post = 12.05
avg_sfw_likes_per_post = 19.59
avg_nsfw_likes_per_post = 7.81
date_most_posts = "2024-01-14"
avg_posts_per_day = 4704.09
likes_percentile = [3, 9, 50]

# Top 100 users data
top_users_data = {'profile_name': ['Yevhen S.', 'Rukia Best Girl', 'Zero zero', 'Burger', 'Naked Ninja', 'b4ai', 'Vi - Vi', 'Dario', 'Catspaws', 'idiotcornball', 'Some Display Name', 'AManApart', 'Teemuu', 'Dreamer', 'Ananda', 'Alan Smithee', 'Magic Studio', 'Versus Z', 'AI MVP', 'GLM2022', 'ronny schipper', 'Maō of Saints', 'Lucifur Bunny', '🦘 dancematd an 🦘', 'wyingjing',
 'Puf', 'Bettie Blasphemy', '', 'somethin', 'yuun', 'blafba', 'Raz', '🤜⚡🤛', 'Dio', 'Elfboi', 'Strikai', 'Joe Momma', 'Ryo', '🔥Ph Hub🔥', 'MC Outlaw (MC Outlaw)', 'AIA', 'Tiago SG', 'Mythos', 'John Silver', '✷', 'Sloppy Joe', 'fortis', 'Megumin', 'BERCOS', 'Dirty', 'DesDc', 'Gimonya', 'Tits and Ass', 'Leonardo Mafra Reina', 'WhyNot Raisins', 'rain', 'Bocah Tua', 'Julia Rubymoon', 'Khutulun', 'muffin zetta', 'Willow', 'Lauriel 🌺', 'EMMANUEL Dacosta', 'Vivio Kaiser', 'Hello 👋 Hello', 'Azusa is cute from birth', 'R', 'Pain&sin', 'D Do', 'Misaki Akeno', 'Bignemo90', 'Hentai Art Ai', 'Mår', 'Alan Hovis', 'Grimaldus', 'ninci (new account)', 'อสูรในสายหมอก', '🟡', 'Abhimanyu', 'Aki', 'SomaC Sel ah. T v2.0 ᴾᵉᵒᵖˡᵉᵃʳᵉˢʰⁱᵗ', '[V]', 'Damien S', 'Izumi Kanto', 'Tsuna', 'veni_vidi_vici_m', 'YoursToPlay', 'Zio', 'Zero', 'Ian Bezziemi', 'JenaUrf', 'Edona', 'Jay Dee', 'Ententom', 'Sin_Scarlet', 'Atti', 'semoxtv', 'ry juice', 'Yugio', 'MAXAM'], 'user_uuid': ['8a33a752-0d4d-4304-9baa-e954db49a159', '5e32cee2-9697-4af7-9fc6-8d7221ba37b9', '1fadcdf9-b0b5-4c53-b272-adc5ad50a61d', '518bffed-0793-43d8-a1a2-ed2ef66550ec', '707af4bc-6590-42ac-ab56-a30b14195b3e', '492c6710-84f8-4d25-8173-4637745bbb40', '6da49b5d-7c5d-4019-a21e-611c879269d3', '13f28181-c510-4b59-8252-250447cdba81', '737af57f-a026-4725-a1f3-fd9577491f8a', '7b8e78ad-2ceb-4f23-a2be-cd4eabb3b708', 'aeeff653-daa4-4f5f-ad72-2ade8496766b', '473fa9e5-35ac-4112-9156-b49ee8224276', 'b9aae266-d509-42e5-be2b-d09195a35756', '8cca3300-6be2-4cf9-a9f9-04871d32ed44', 'c236b7a2-69d5-49fc-ad2d-0281a0e5b29c', 'd4be5799-1c43-4420-a3b2-2697eb99429f', '34b41b77-c345-4c5d-9518-71a09bfda8e5', '09c122e8-51e7-4578-9cfc-351e15ff6bdf', '07168cd3-f5ae-4b81-8171-dbb411b715e0', '842a45e6-edff-47b1-a379-74a931ffa2a0', '1c4580b2-6145-40a5-924f-4faec29971a7', 'f194e0cd-1d7f-4d4b-bd33-dd3f4d910c80', 'b6536b6a-31fa-4c67-a96b-be97b3e726e0', 'e1e9c0c0-cbe3-4d6d-b07a-d0feae1a7cd8', '8915f501-1fea-4f0b-bf48-b32ef27443c9', 'ddae3b36-f3ec-4ee0-8d53-91cd579bc760', '6c9eb40c-a451-4c73-b364-9103e1b8819e', '58104f03-f2b7-42bb-a3aa-2e9a55838bc2', '0222d673-0a40-4e58-aaea-c9b3cc36f0e4', 'e4829ffb-7420-4f49-bb03-0332bcd69cdb', 'e68633ad-2086-40f2-9b02-d7e5a041b169', 'a8f98b54-0677-4bc4-bd74-ac68fe234116', 'bbbdf4b5-81e3-488d-abda-ac58e7cf1b56', 'eedf979c-10f9-4562-b2f9-93bd79db1428', '6fb420ba-ecbf-487a-a9c6-a4afeb8f6659', 'f90baa87-a5c8-4db1-a22e-398296313043', '14fed926-805c-4429-ac34-ba93b5242ce3', '82648d4e-c847-4a82-9670-41e758622721', '60f5ab4c-8b3a-4bc8-94ae-64f653a09e26', '1c4b5bdf-2bcc-4b9e-83cd-efa0e6ed2019', 'eb1900d9-c6ea-42a7-aaa1-09108ecfc15b', 'f5f0b1b6-a90a-417c-b9aa-9dc57ed2482d', '96bb7db3-0750-486b-9510-50a1a450a6a0', 'b47bc1ab-bdc3-4397-9aad-e1516f5691f8', '67077fb7-6267-4ca2-bb45-95ff15cf3189', '5f22910b-8734-4759-bddd-b75f0706b4f3', '38241e5d-5d73-49f2-accc-d67ed6b8956d', '5b1acaa1-26fe-4664-ac3d-d0f181aaa933', '9dc191d5-c4ee-474f-9776-0634d0b59efb', '7a183bb5-7941-49eb-a42c-73bb1423253e', '514f5e11-ddd1-4268-986d-c9b124223756', 'cd8d8ed7-864d-4b92-abe5-c1ea60e7276b', 'e5a7fe40-1528-4561-9d35-76fdf20f736b', 'c19f174f-ef6f-481b-b7a3-ccbf92acb5c8', '9382d75a-2bd9-45c5-be04-0829d60af145', '4ed5472a-df3e-476e-beff-5f40c23ec54b', '49ef0992-1427-409a-9a06-f355370f7673', '7f1d07ed-3e83-42c3-9bc4-94658595b7a5', '89d74016-38b0-46e1-86db-2a71b0780d08', 'e7dce258-5b84-4c04-8653-bd5b3d7474d6', 'e356be6c-e598-46ae-a136-78eeca5d81e7', '06fce36d-1910-4fb4-aa7e-807c10715961', '93572140-b85b-42b0-9f71-b739dbbcc734', 'be6cb0c1-5ebe-4cd8-8422-d9d35740ec7b', '24646f3c-0deb-4446-a91d-d6a283c60e42', 'd5cd8d57-9f6d-498f-84ac-21dbe1a60688', 'a2e0f01a-62ae-469e-8a2f-eef4eddc3516', 'f0e1c6fd-2acb-4a86-be74-1678bf4911be', '681d2fa1-30e9-4844-833a-52001bb3587a', '44979c02-5e45-4f96-95b2-111e379b4756', 'cc76f5c2-74ad-4103-9365-55ce05987270', '6a353ffd-bd77-4684-b053-237971a21d8b', '6bff2b87-735d-40f1-8201-0ac207ce8c74', '7b83bd40-f77b-4d32-afc2-b4ea2d6832c6', '648ccb71-fb09-45c7-9778-35441b53482f', 'b379150c-e275-43f1-914c-4c795b1b4f58', 'c32c9ba6-15f8-466e-bd08-d367ef50a0cd', 'c0f5ba69-c699-40f7-bb3c-b478c7bd2671', '20047062-e3b5-4848-8078-6a8f728e731f', '63e1e5d8-5158-4da9-a1a3-2eb94bc03f9b', '7a274a0a-b67b-4de8-9953-203576e25a7f', '31e15480-43d6-4b4c-b960-d81f97791bd5', '49e4ddc1-19f8-4d97-bd46-ff6db1f51eca', '73bc8052-e36a-4809-baac-4773dfdab614', '7d507973-411e-4014-908e-ca616392f919', 'a9bee5f0-44ed-46b8-b59e-76ff14e14c1f', '68af5e56-e179-4140-babb-68637d4f2908', '6567562d-b83a-4799-bcfd-f774045f58c4', '157b4840-10da-475a-a6e6-6a09382a2229', 'bb3eaff9-8770-4996-bdf8-a0004f925c6e', '7c6a73f5-d7ce-4900-b53c-96507502c7b1', 'c73d7632-7e9f-4a1a-a478-b040b2753f09', '824c619f-b11d-4a94-a59f-d5d1c32eede2', 'd9fdb886-349a-4f9a-b9e5-faedfbbf67b6', 'e00d56fd-da8a-45a5-86fd-980574a056b3', '204f3ee2-47b8-42a2-b62c-b767dc6f59fa', 'c715a317-e9e1-4a55-8c5c-0915c67273e9', '62cfc41d-948a-4bb6-b4be-3c4557e4897f', '3f50fbb0-5e05-48f1-a889-dcc7d2807ce3', '0ce1d264-d764-40ab-aeda-3ec2e9b616c1'], 'post_count': [30084, 23919, 15396, 14655, 13304, 10624, 9274, 9132, 8407, 8329, 8236, 7244, 7121, 6675, 6662, 6638, 6322, 6223, 6037, 6008, 5879, 5673, 5395, 5315, 5250, 5212, 4998, 4972, 4857, 4841, 4814, 4764, 4756, 4703, 4529, 4432, 4255, 4248, 4083, 4071, 4024, 3975, 3880, 3851, 3809, 3750, 3736, 3736, 3664, 3635, 3577, 3564, 3511, 3497, 3394, 3379, 3365, 3314, 3250, 3245, 3230, 3182, 3162, 3113, 3072, 3046, 3040, 3025, 3010, 2977, 2947, 2896, 2883, 2873, 2850, 2836, 2836, 2824, 2822, 2816, 2807, 2796, 2784, 2763, 2746, 2724, 2722, 2703, 2699, 2669, 2662, 2660, 2639, 2637, 2613, 2608, 2582, 2581, 2578, 2569]}
top_users_df = pd.DataFrame(top_users_data)

top_users_likes = {'profile_name': ['Zero zero', 'Amaiko Ayakashi', 'Teemuu', '🔥Ph Hub🔥', 'Hello 👋 Hello', 'Maō of Saints', 'ry juice', 'Puf', 'timbles', 'Elara the Mage 🪄', 'Izumi Kanto', 'scoot🛵', 'HeisMad', 'Julia Rubymoon', 'wyin gjing', '🦒Giraffe Boi Danny🦒', 'Bocah Tua', 'Rukia Best Girl', 'veni_vidi_vici_m', 'Mirror', 'Wolf (El Wolfo)', 'Grimaldus', 'Siddorf', 'Vex 🐇', 'NSFW Paradise', 'ninci (new account)', 'PPX', 'Ij', 'ry k', 'EvaClausAI', 'still dope', 'Yevhen S.', '[V]', 'Autumn', 'Misaki Akeno', 'Milunya Essence', '🦘 dancematdan 🦘', 'Brad', 'Prime', 'Amish', 'Ecchiman',   'Remilia', 'The Cute in Yellow', '🐐Lucifer🐐', 'rain', 'Zero<(=⩊=)>', 'Aki', 'Speedlife', 'Temperance', '✨Hexy✨', 'Lilianna', 'Natchu', 'Katnip', 'six', 'Takuu', '𝓜𝓪𝓽𝓱𝓮𝔀 𝓒 - 𝓣𝓲𝓶𝓮 𝓦𝓲𝔃𝓪𝓻𝓭🧙\u200d♂️', 'Risu', 'Leonardo Mafra                  Reina', 'Ryo', 'Rae 屈愛', 'Naked Ninja', 'Stregal', 'Some Display Name', 'Gerson D. Rider', 'Willow', 'Senlin', '1818 🌟 [SDガール]', '', 'Nini', 'Degrees of difference', 'Through the fire', 'LauLau', 'Burgahr', 'Iroha', 'AKIRA', 'Langaku', 'Call_Me_Toni', 'Ananda', 'shadow0667', 'Tired Puppy', 'Catspaws', 'Tivadar', '-FreaknesS-', 'Alicia', 'Akiyoshi', 'Sigurd', 'Kirbynator', 'Bettie Blasphemy', 'BERCOS', 'Phlyer', '🎸☯️ Yinyin ☯️🎸', 'semoxtv', '\u200c', 'Zablinski', '''𝔸� 𝕥𝕚𝕤𝕥𝕚𝕔  𝕤𝕡𝕖
𝕔𝕥𝕒𝕥𝕠𝕣''', 'Jordan_M', 'Dario', '', 'Majin de Géminis', 'Noxi'], 'user_uuid': ['1fadcdf9-b0b5-4c      53-b272-adc5ad50a61d', '0fee7fab-9ca0-484e-9994-eb5e04ceb8f5', 'b9aae266-d509-42e5-be2b-d09195a35756', '60f5ab4c-8b3a-4bc8-94ae-64f653a09e26', '24646f3c-0deb-4446-a91d-d6a283c60e42', 'f194e0cd-1d7f-4d4b-bd33-dd3f4d910c80', '62cfc41d-948a-4bb6-b4be-3c4557e4897f', 'ddae3b36-f3ec-4ee0-8d53-91cd579bc760', 'ee6e0470-2144-4648-83d1-f64e8ab3a801', 'a06f278b-7781-43a4-87cb-5354925afa96', '73bc8052-e36a-4809-baac-4773dfdab614', 'c0a8be3c-cadd-437d-9624-97f80635b354', 'dddde05a-172e-41cf-a07a-269f9f0cf1a7', '7f1d07ed-3e83-42c3-9bc4-94658595b7a5', '8915f501-1fea-4f0b-bf48-b32ef27443c9', '531e6a5e-9be6-473e-aa7b-2f49ccb80146', '49ef0992-1427-409a-9a06-f355370f7673', '5e32cee2-9697-4af7-9fc6-8d7221ba37b9', 'a9bee5f0-44ed-46b8-b59e-76ff14e14c1f', 'a8deac57-4ac6-4115-afc5-c5fe434623a1', '79136320-5864-47ea-827b-6d25a279bbd1', '648ccb71-fb09-45c7-9778-35441b53482f', '9d163c8e-51c9-47c2-a488-fe49004d00ae', '2788f315-7f17-487a-b26c-64cb09c001f2', '26bcb655-f436-4b0e-8414-62e0aea8b0e7', 'b379150c-e275-43f1-914c-4c795b1b4f58', '0833625b-ea56-4b2e-a8a7-64abea9bf1a2', '35dd6225-0a2f-4872-b9da-256cd1cf8b34', '9110105a-1c2b-4527-8cdd-63abdba9a7b0', '7e243e76-3d9f-4b09-8926-a5698cc87011', 'd603d665-89ff-4d79-aa69-11172abb9f50', '8a33a752-0d4d-4304-9baa-e954db49a159', '31e15480-43d6-4b4c-b960-d81f97791bd5', 'ed88199e-ee45-4636-bea5-266614ca62ba', '44979c02-5e45-4f96-95b2-111e379b4756', '11f63b9e-7349-411b-b518-3ebd3324bab3', 'e1e9c0c0-cbe3-4d6d-b07a-d0feae1a7cd8', 'b23d146a-89e2-4f36-9a3c-b714b766423c', '3f13ac7d-0798-4ae8-8b56-1e06ab0cba36', '7d7c2b75-b0f3-480f-af58-0059c43b6f88', 'c811e82d-0612-4e6f-9805-a8b3dfe4afd3', '8a2119bc-6e1b-49c5-a1e0-d62c01497a07', '15db6cd2-8ff7-42f1-917f-b43c203f675b', '5fa14a22-43bf-499a-9f0f-2b34a8d23576', '4ed5472a-df3e-476e-beff-5f40c23ec54b', '9ca45e8e-7981-4539-bbab-86310eeb88a1', '63e1e5d8-5158-4da9-a1a3-2eb94bc03f9b', '0f6da447-6a28-4af0-8e62-897c6f66953c', 'e4a3f042-0c35-40c1-95c9-7497b86bbb87', '7b3676aa-ef73-4205-a698-820a2d658a44', '229f6660-c66b-459a-842b-a944577f51cf', '663af217-0b4a-40fd-a51f-394191ec2bec', '609c9c02-96bf-4e8d-a7cd-44b3a8a88ae9', 'ae584f4e-55c5-4977-aab0-8d3c5b5d52ad', '96bc934f-eb26-4909-8208-5a7ffe99ac21', '2e2712b0-1b44-4c4c-bd48-59f6a2ff4f28', 'e0a8dc0d-24b2-427e-b1ed-87bdf136b9ac', 'c19f174f-ef6f-481b-b7a3-ccbf92acb5c8', '82648d4e-c847-4a82-9670-41e758622721', '4785a75b-aa47-4bef-9dc9-4edc8f19f2b3', '707af4bc-6590-42ac-ab56-a30b14195b3e', '2ce5a235-3b49-4d19-94cc-82a51f608bef', 'aeeff653-daa4-4f5f-ad72-2ade8496766b', '0f48626a-893a-4906-97bc-e3122f2474e9', 'e356be6c-e598-46ae-a136-78eeca5d81e7', 'b0c03c3e-e566-4ac5-916b-21db43d56ba0', '4da3968c-9bf4-47f9-93c7-343262a5638a', 'b5cbaff5-2601-4a10-89a5-f5a269fe42ae', '24d7061e-acd0-4b68-a0ab-13f235c5593e', '2811f638-4e0a-4fb6-8b54-843402da01d0', '25a64ac5-14d3-4f69-8284-4c123048f2bc', '3f288873-8b0f-412c-a56a-d469c43fee73', '6f1a492e-dd1b-400e-b11b-2cbd7d16dd47', '5fd9967b-d576-498a-8fc4-b508e30423e3', '231e8ae4-4561-400e-b1f7-9ba1b40230b2', '7426396e-5f91-4fd0-89b3-4a043c004ac4', 'a31501cd-c646-4d2f-9576-93512f0bfe5c', 'c236b7a2-69d5-49fc-ad2d-0281a0e5b29c', '7d92174f-b616-4688-a2b1-aea1c05aa301', '4b5df674-9db1-44b5-b997-4feb6ce60865', '737af57f-a026-4725-a1f3-fd9577491f8a', '83c5ff95-2589-471d-ab40-cb600f3a8772', 'feff31d9-af0e-4fa0-b3e0-f4a4767d983e', '7ada8088-4be5-425d-804d-303c27b97821', '4a931d9e-1fdb-493a-abf8-1502f7d2bf13', '25d4b36f-8268-4c52-8a91-58247484eb20', '05a5e6d1-6032-4e2a-8477-0f050548aa35', '6c9eb40c-a451-4c73-b364-9103e1b8819e', '9dc191d5-c4ee-474f-9776-0634d0b59efb', '6c3b8bdb-1e6e-455e-8841-d6c79139b4fd', '338f158e-d839-4dd6-9fca-f8e2cfcecec4', 'c715a317-e9e1-4a55-8c5c-0915c67273e9', 'fe2b24f8-9086-4dff-ae87-f7e02dabf555', 'a0665e8c-167c-4d37-a45f-37bf4a5dc663', 'c3744dec-e334-4a10-8917-be3edf5baacc', 'a511fc91-6e8b-41a5-bfff-245d3a08b252', '13f28181-c510-4b59-8252-250447cdba81', '58104f03-f2b7-42bb-a3aa-2e9a55838bc2', 'bf9b05cf-f9fb-40c0-9de4-3eab88f7e052', 'b4c3530c-2bf4-4936-a2cf-53ddd1e767eb'], 'likes_count': [456997, 427268, 270952, 253993, 243648, 229908, 226800, 197927, 197865, 194463, 190725, 183104, 180058, 175794, 162692, 162142, 157158, 153354, 152690, 142600, 139269, 136590, 136100, 135462, 134980, 131850, 121453, 116320, 114606, 111705, 106505, 106476, 103586, 98248, 97536, 94676, 92281, 91390, 89999, 87231, 86214, 86167, 84746, 83707, 83141, 82089, 81926, 79175, 78275, 78050, 77678, 77119, 76777, 76416, 76152, 74353, 72581, 70812, 70418, 69786, 69083, 68414, 68333, 67688, 66388, 65795, 65158, 63706, 63436, 63400, 63268, 63150, 62794, 62389, 61795, 61112, 60475, 57905, 57491, 57009, 56992, 56286, 55563, 55496, 55091, 54927, 54844, 54789, 54360, 53980, 53967, 53726, 52902, 52652, 52487, 52486, 51840, 50556, 50101, 49502]}
top_users_likes_df = pd.DataFrame(top_users_likes)

# Posts by day data
posts_by_day_data = {'date': ['2022-10-03', '2022-10-04', '2022-10-05', '2022-10-06', '2022-10-07', '2022-10-08', '2022-10-09', '2022-10-10', '2022-10-11', '2022-10-12', '2022-10-13', '2022-10-14', '2022-10-15', '2022-10-16', '2022-10-17', '2022-10-18', '2022-10-19', '2022-10-20', '2022-10-21', '2022-10-22', '2022-10-23', '2022-10-24', '2022-10-25', '2022-10-26', '2022-10-27', '2022-10-28', '2022-10-29', '2022-10-30', '2022-10-31', '2022-11-01', '2022-11-02', '2022-11-03', '2022-11-04', '2022-11-05', '2022-11-06', '2022-11-07', '2022-11-08', '2022-11-09', '2022-11-10', '2022-11-11', '2022-11-12', '2022-11-13', '2022-11-14', '2022-11-15', '2022-11-16', '2022-11-17', '2022-11-18', '2022-11-19', '2022-11-20', '2022-11-21', '2022-11-22', '2022-11-23', '2022-11-24', '2022-11-25', '2022-11-26', '2022-11-27', '2022-11-28', '2022-11-29', '2022-11-30', '2022-12-01', '2022-12-02', '2022-12-03', '2022-12-04', '2022-12-05', '2022-12-06', '2022-12-07', '2022-12-08', '2022-12-09', '2022-12-10', '2022-12-11', '2022-12-12', '2022-12-13', '2022-12-14', '2022-12-15', '2022-12-16', '2022-12-17', '2022-12-18', '2022-12-19', '2022-12-20', '2022-12-21', '2022-12-22', '2022-12-23', '2022-12-24', '2022-12-25', '2022-12-28', '2022-12-29', '2022-12-30', '2022-12-31', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12', '2023-01-13', '2023-01-14', '2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20', '2023-01-21', '2023-01-22', '2023-01-23', '2023-01-24', '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-28', '2023-01-29', '2023-01-30', '2023-01-31', '2023-02-01', '2023-02-02', '2023-02-03', '2023-02-04', '2023-02-05', '2023-02-06', '2023-02-07', '2023-02-08', '2023-02-09', '2023-02-10', '2023-02-11', '2023-02-12', '2023-02-13', '2023-02-14', '2023-02-15', '2023-02-16', '2023-02-17', '2023-02-18', '2023-02-19', '2023-02-20', '2023-02-21', '2023-02-22', '2023-02-23', '2023-02-24', '2023-02-25', '2023-02-26', '2023-02-27', '2023-02-28', '2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05', '2023-03-06', '2023-03-07', '2023-03-08', '2023-03-09', '2023-03-10', '2023-03-11', '2023-03-12', '2023-03-13', '2023-03-14', '2023-03-15', '2023-03-16', '2023-03-17', '2023-03-18', '2023-03-19', '2023-03-20', '2023-03-21', '2023-03-22', '2023-03-23', '2023-03-24', '2023-03-25', '2023-03-26', '2023-03-27', '2023-03-28', '2023-03-29', '2023-03-30', '2023-03-31', '2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', '2023-04-13', '2023-04-14', '2023-04-15', '2023-04-16', '2023-04-17', '2023-04-18', '2023-04-19', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25', '2023-04-26', '2023-04-27', '2023-04-28', '2023-04-29', '2023-04-30', '2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05', '2023-05-06', '2023-05-07', '2023-05-08', '2023-05-09', '2023-05-10', '2023-05-11', '2023-05-12', '2023-05-13', '2023-05-14', '2023-05-15', '2023-05-16', '2023-05-17', '2023-05-18', '2023-05-19', '2023-05-20', '2023-05-21', '2023-05-22', '2023-05-23', '2023-05-24', '2023-05-25', '2023-05-26', '2023-05-27', '2023-05-28', '2023-05-29', '2023-05-30', '2023-05-31', '2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05', '2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-10', '2023-06-11', '2023-06-12', '2023-06-13', '2023-06-14', '2023-06-15', '2023-06-16', '2023-06-17', '2023-06-18', '2023-06-19', '2023-06-20', '2023-06-21', '2023-06-22', '2023-06-23', '2023-06-24', '2023-06-25', '2023-06-26', '2023-06-27', '2023-06-28', '2023-06-29', '2023-06-30', '2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06', '2023-07-07', '2023-07-08', '2023-07-09', '2023-07-10', '2023-07-11', '2023-07-12', '2023-07-13', '2023-07-14', '2023-07-15', '2023-07-16', '2023-07-17', '2023-07-18', '2023-07-19', '2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24', '2023-07-25', '2023-07-26', '2023-07-27', '2023-07-28', '2023-07-29', '2023-07-30', '2023-07-31', '2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05', '2023-08-06', '2023-08-07', '2023-08-08', '2023-08-09', '2023-08-10', '2023-08-11', '2023-08-12', '2023-08-13', '2023-08-14', '2023-08-15', '2023-08-16', '2023-08-17', '2023-08-18', '2023-08-19', '2023-08-20', '2023-08-21', '2023-08-22', '2023-08-23', '2023-08-24', '2023-08-25', '2023-08-26', '2023-08-27', '2023-08-28', '2023-08-29', '2023-08-30', '2023-08-31', '2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04', '2023-09-05', '2023-09-06', '2023-09-07', '2023-09-08', '2023-09-09', '2023-09-10', '2023-09-11', '2023-09-12', '2023-09-13', '2023-09-14', '2023-09-15', '2023-09-16', '2023-09-17', '2023-09-18', '2023-09-19', '2023-09-20', '2023-09-21', '2023-09-22', '2023-09-23', '2023-09-24', '2023-09-25', '2023-09-26', '2023-09-27', '2023-09-28', '2023-09-29', '2023-09-30', '2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05', '2023-10-06', '2023-10-07', '2023-10-08', '2023-10-09', '2023-10-10', '2023-10-11', '2023-10-12', '2023-10-13', '2023-10-14', '2023-10-15', '2023-10-16', '2023-10-17', '2023-10-18', '2023-10-19', '2023-10-20', '2023-10-21', '2023-10-22', '2023-10-23', '2023-10-24', '2023-10-25', '2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29', '2023-10-30', '2023-10-31', '2023-11-01', '2023-11-02', '2023-11-03', '2023-11-04', '2023-11-05', '2023-11-06', '2023-11-07', '2023-11-08', '2023-11-09', '2023-11-10', '2023-11-11', '2023-11-12', '2023-11-13', '2023-11-14', '2023-11-15', '2023-11-16', '2023-11-17', '2023-11-18', '2023-11-19', '2023-11-20', '2023-11-21', '2023-11-22', '2023-11-23', '2023-11-24', '2023-11-25', '2023-11-26', '2023-11-27', '2023-11-28', '2023-11-29', '2023-11-30', '2023-12-01', '2023-12-02', '2023-12-03', '2023-12-04', '2023-12-05', '2023-12-06', '2023-12-07', '2023-12-08', '2023-12-09', '2023-12-10', '2023-12-11', '2023-12-12', '2023-12-13', '2023-12-14', '2023-12-15', '2023-12-16', '2023-12-17', '2023-12-18', '2023-12-19', '2023-12-20', '2023-12-21', '2023-12-22', '2023-12-23', '2023-12-24', '2023-12-25', '2023-12-26', '2023-12-27', '2023-12-28', '2023-12-29', '2023-12-30', '2023-12-31', '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30', '2024-01-31', '2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', '2024-02-05', '2024-02-06', '2024-02-07', '2024-02-08', '2024-02-09', '2024-02-10', '2024-02-11', '2024-02-12', '2024-02-13', '2024-02-14', '2024-02-15', '2024-02-16', '2024-02-17', '2024-02-18', '2024-02-19', '2024-02-20', '2024-02-21', '2024-02-22', '2024-02-23', '2024-02-24', '2024-02-25', '2024-02-26', '2024-02-27', '2024-02-28', '2024-02-29', '2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05', '2024-03-06', '2024-03-07', '2024-03-08', '2024-03-09', '2024-03-10', '2024-03-11', '2024-03-12', '2024-03-13', '2024-03-14', '2024-03-15', '2024-03-16', '2024-03-17', '2024-03-18', '2024-03-19', '2024-03-20', '2024-03-21', '2024-03-22', '2024-03-23', '2024-03-24', '2024-03-25', '2024-03-26', '2024-03-27'], 'total_posts': [7, 3, 4, 21, 54, 53, 58, 61, 20, 62, 28, 61, 17, 20, 11, 34, 45, 60, 42, 48, 34, 44, 45, 60, 33, 55, 50, 72, 42, 55, 27, 46, 53, 41, 51, 90, 84, 101, 74, 53, 53, 70, 62, 54, 53, 41, 123, 212, 221, 47, 81, 125, 117, 65, 59, 53, 85, 49, 45, 25, 100, 75, 85, 60, 53, 70, 67, 94, 56, 75, 48, 44, 80, 128, 124, 92, 133, 208, 119, 104, 63, 100, 169, 101, 4, 76, 74, 71, 96, 223, 74, 123, 193, 294, 98, 153, 130, 83, 138, 80, 142, 284, 314, 278, 289, 342, 396, 387, 317, 411, 1096, 914, 900, 881, 771, 1206, 640, 1133, 631, 602, 678, 693, 1117, 907, 1077, 1137, 1086, 1421, 1439, 1523, 1209, 1607, 1349, 1817, 1646, 1140, 1765, 1560, 1573, 1367, 1590, 1702, 1804, 1824, 1640, 1905, 1859, 2020, 1581, 2153, 2100, 2044, 1849, 1859, 1941, 2078, 2302, 2261, 1878, 1862, 2081, 2154, 3756, 3222, 2823, 2804, 2608, 3391, 4212, 3497, 4007, 3526, 3034, 4329, 4684, 3058, 3710, 2905, 3376, 3928, 4274, 4112, 4073, 4068, 3540, 4174, 4209, 3731, 4526, 4567, 5049, 4162, 3788, 3950, 4529, 4148, 4304, 3637, 3368, 3294, 3337, 3830, 3801, 3053, 2954, 2701, 2908, 3146, 2899, 3431, 3295, 3604, 3108, 3559, 3619, 3583, 4555, 3885, 3986, 3713, 2810, 3813, 3542, 4135, 3550, 3380, 3582, 4110, 4524, 4978, 3995, 4319, 4905, 5194, 5138, 5172, 4452, 4636, 4216, 4963, 4243, 4138, 3844, 4528, 3882, 3817, 4119, 3947, 3691, 3474, 3957, 4136, 4635, 5247, 4084, 3637, 3770, 3922, 4326, 4188, 4416, 4393, 4414, 4092, 3930, 4434, 4319, 3841, 4030, 4051, 3890, 4607, 4504, 4494, 5077, 5107, 4515, 5219, 4742, 4739, 4872, 4392, 5432, 4445, 4321, 4973, 5240, 5680, 5373, 4911, 4411, 3933, 4859, 5819, 4891, 4897, 5000, 5231, 4900, 6365, 5197, 4700, 4383, 6221, 5798, 5479, 5859, 5012, 5237, 4600, 5349, 5384, 4690, 6159, 5187, 6221, 5429, 5652, 5572, 5722, 5464, 5716, 5506, 5502, 5506, 5607, 6496, 5421, 6265, 5862, 5267, 5222, 5438, 5992, 6562, 6406, 6298, 6138, 6513, 5893, 6069, 5868, 6330, 5848, 5531, 5903, 5248, 5956, 5780, 5726, 4680, 5319, 5823, 5573, 5444, 5618, 5785, 5202, 4641, 5517, 5303, 5630, 5408, 6024, 6074, 6293, 6330, 6297, 6336, 6056, 6096, 6156, 6084, 6174, 6216, 6527, 6866, 6428, 6747, 6616, 6501, 6859, 6659, 6529, 6940, 6800, 6888, 7380, 7470, 6904, 7607, 7278, 6957, 7281, 7128, 7293, 8237, 7471, 7121, 7835, 7400, 7724, 7770, 8224, 8091, 8282, 8067, 7741, 7331, 7685, 8029, 7495, 7442, 7795, 7872, 8146, 8615, 8185, 8710, 8789, 8079, 7952, 7410, 7334, 7862, 8138, 8395, 8270, 8523, 8693, 8303, 9443, 7793, 8041, 8455, 7921, 8559, 8208, 8427, 9264, 8839, 8914, 8746, 7846, 8908, 8614, 8740, 9376, 9279, 8967, 9071, 9628, 9596, 8932, 9426, 10260, 9905, 10280, 10313, 10226, 10472, 10825, 9874, 9215, 9794, 10245, 11111, 10245, 10145, 9706, 9707, 10149, 9983, 9869, 9689, 9346, 8622, 9597, 9017, 9997, 9638, 9651, 9623, 9051, 8992, 9118, 8984, 9199, 8441, 9015, 8851, 8715, 8872, 8952, 9482, 9131, 9122, 9807, 10225, 9957, 10219, 9802, 10145, 10266, 10221, 10772, 10396, 10708, 10916, 9982, 9587, 9543, 8632, 9492, 9323, 9816, 9661, 9372, 9591, 9603, 9612, 9741, 9774, 9061, 10072, 9985, 10090, 9363, 9356, 9571, 9615, 9388, 9208, 9115, 9446, 9872, 10187, 9585, 9891, 5633], 'nsfw_posts': [0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 2, 0, 1, 1, 1, 0, 3, 3, 3, 1, 3, 5, 5, 0, 1, 6, 4, 3, 5, 2, 5, 8, 5, 6, 1, 9, 3, 2, 1, 9, 7, 8, 11, 7, 3, 19, 33, 62, 20, 33, 58, 73, 41, 40, 35, 45, 39, 26, 15, 59, 35, 42, 37, 24, 43, 37, 64, 27, 56, 34, 23, 41, 103, 97, 66, 104, 160, 93, 84, 37, 85, 139, 55, 3, 63, 42, 67, 68, 76, 27, 88, 140, 220, 80, 99, 83, 68, 111, 56, 121, 269, 283, 248, 258, 304, 341, 344, 273, 355, 1014, 775, 790, 788, 689, 1091, 578, 1041, 522, 449, 543, 559, 979, 668, 900, 947, 873, 1209, 1197, 1223, 956, 1299, 1080, 1472, 1428, 956, 1489, 1300, 1268, 1116, 1359, 1267, 1523, 1575, 1452, 1553, 1510, 1611, 1239, 1784, 1833, 1711, 1553, 1524, 1606, 1772, 1930, 1866, 1492, 1494, 1636, 1763, 3154, 2790, 2426, 2408, 2204, 2784, 3847, 3088, 3405, 2938, 2535, 3444, 4026, 2617, 3077, 2460, 2811, 3398, 3812, 3524, 3318, 3457, 2926, 3532, 3398, 3008, 3579, 3397, 3914, 3497, 2901, 3158, 3658, 3229, 3385, 2783, 2685, 2570, 2644, 2973, 2761, 2420, 2389, 2078, 2366, 2363, 2256, 2192, 2281, 2570, 2235, 2396, 2600, 2750, 3612, 2870, 3026, 2709, 1849, 2858, 2577, 2771, 2665, 2406, 2298, 3086, 3381, 3798, 3025, 3285, 3823, 3978, 3909, 3738, 3111, 3508, 3109, 3546, 3059, 2763, 3024, 3408, 2820, 2847, 3280, 2973, 2504, 2420, 2867, 3028, 3480, 3620, 2849, 2497, 2532, 2682, 2746, 2580, 2813, 2850, 2932, 2555, 2479, 2881, 2528, 2432, 2490, 2584, 2417, 3093, 3072, 2819, 3525, 3313, 2936, 3319, 2982, 3214, 3451, 2634, 3580, 2841, 2786, 3224, 3592, 3582, 3409, 3242, 2761, 2436, 3305, 3893, 3094, 3179, 3290, 2952, 2895, 4251, 3532, 3120, 2609, 3702, 3200, 3358, 3511, 2995, 3145, 2743, 3199, 3290, 2748, 3697, 3249, 3579, 3009, 3376, 3331, 3334, 3441, 3410, 3103, 3140, 3375, 3394, 4004, 3249, 4138, 3361, 3196, 3334, 3328, 3486, 3803, 4226, 4004, 3688, 4027, 3529, 3825, 3677, 4063, 3870, 3621, 3694, 3366, 3490, 3581, 3774, 2676, 3151, 3606, 3132, 3080, 3159, 3481, 3120, 2848, 3397, 3135, 3131, 3345, 3622, 3936, 3759, 3926, 3976, 3639, 3574, 3602, 3486, 3444, 3499, 3546, 3973, 3769, 3393, 3903, 3547, 3486, 3877, 3787, 3849, 4195, 4162, 4137, 4639, 4817, 4232, 4554, 4296, 4331, 4487, 4560, 4638, 5180, 4685, 4276, 5158, 4648, 4963, 4626, 5121, 4847, 4990, 4976, 4667, 4658, 4745, 5041, 4545, 4576, 4589, 4865, 5083, 5455, 4904, 5048, 5026, 4720, 4639, 4316, 4361, 4763, 4959, 5051, 5203, 5049, 5265, 5048, 5409, 4640, 4685, 5282, 4713, 5095, 4784, 5062, 5792, 5317, 5566, 5323, 4727, 5429, 5211, 5649, 6218, 6173, 5753, 5942, 5858, 5943, 5415, 5920, 6513, 6208, 6662, 6142, 6094, 6122, 6752, 5922, 5202, 5979, 6488, 6961, 6162, 6315, 6230, 5911, 6049, 6017, 6018, 5414, 5053, 4855, 5687, 5243, 6046, 5820, 5690, 5860, 5595, 5345, 5380, 5657, 5535, 5191, 5501, 5223, 5272, 5637, 5590, 6136, 5903, 5669, 6049, 6467, 6166, 6111, 6059, 6432, 6295, 6579, 6713, 6441, 6616, 6655, 5996, 5477, 5601, 4841, 5549, 5644, 5923, 5698, 5588, 5492, 5570, 5602, 6159, 6019, 5470, 6329, 6080, 6389, 5661, 5745, 6067, 5996, 5858, 5250, 5231, 5763, 5925, 6129, 5654, 6243, 3246], 'nsfw_percentage': [0.0, 0.0, 0.0, 4.761905, 0.0, 0.0, 5.172414, 0.0, 0.0, 0.0, 0.0, 3.278689, 0.0, 5.0, 9.090909, 2.941176, 0.0, 5.0, 7.142857, 6.25, 2.941176, 6.818182, 11.111111, 8.333333, 0.0, 1.818182, 12.0, 5.555556, 7.142857, 9.090909, 7.407407, 10.869565, 15.09434, 12.195122, 11.764706, 1.111111, 10.714286, 2.970297, 2.702703, 1.886792, 16.981132, 10.0, 12.903226, 20.37037, 13.207547, 7.317073, 15.447154, 15.566038, 28.054299, 42.553191, 40.740741, 46.4, 62.393162, 63.076923, 67.79661, 66.037736, 52.941176, 79.591837, 57.777778, 60.0, 59.0, 46.666667, 49.411765, 61.666667, 45.283019, 61.428571, 55.223881, 68.085106, 48.214286, 74.666667, 70.833333, 52.272727, 51.25, 80.46875, 78.225806, 71.73913, 78.195489, 76.923077, 78.151261, 80.769231, 58.730159, 85.0, 82.248521, 54.455446, 75.0, 82.894737, 56.756757, 94.366197, 70.833333, 34.080717, 36.486486, 71.544715, 72.53886, 74.829932, 81.632653, 64.705882, 63.846154, 81.927711, 80.434783, 70.0, 85.211268, 94.71831, 90.127389, 89.208633, 89.273356, 88.888889, 86.111111, 88.888889, 86.119874, 86.374696, 92.518248, 84.792123, 87.777778, 89.443814, 89.364462, 90.464345, 90.3125, 91.879965, 82.725832, 74.584718, 80.088496, 80.663781, 87.645479, 73.649394, 83.56546, 83.289358, 80.38674, 85.080929, 83.182766, 80.302035, 79.073615, 80.833852, 80.059303, 81.012658, 86.755772, 83.859649, 84.362606, 83.333333, 80.610299, 81.638625, 85.471698, 74.441833, 84.423503, 86.348684, 88.536585, 81.52231, 81.226466, 79.752475, 78.368121, 82.861124, 87.285714, 83.708415, 83.991347, 81.979559, 82.740855, 85.274302, 83.840139, 82.529854, 79.446219, 80.236305, 78.61605, 81.847725, 83.972311, 86.592179, 85.936947, 85.877318, 84.509202, 82.099676, 91.334283, 88.304261, 84.976291, 83.32388, 83.553065, 79.55648, 85.952178, 85.57881, 82.938005, 84.681583, 83.264218, 86.507128, 89.190454, 85.700389, 81.463295, 84.980334, 82.655367, 84.61907, 80.731765, 80.621817, 79.076447, 74.381432, 77.520301, 84.022105, 76.583949, 79.949367, 80.768382, 77.844744, 78.64777, 76.519109, 79.720903, 78.020644, 79.232844, 77.624021, 72.638779, 79.266295, 80.873392, 76.934469, 81.361761, 75.111252, 77.819938, 63.888079, 69.2261, 71.309656, 71.911197, 67.322282, 71.843051, 76.751326, 79.297475, 73.873874, 75.915705, 72.959871, 65.800712, 74.954104, 72.755505, 67.013301, 75.070423, 71.183432, 64.154104, 75.085158, 74.734748, 76.295701, 75.71965, 76.059273, 77.940877, 76.588371, 76.080187, 72.273782, 69.878706, 75.66868, 73.742884, 71.448721, 72.095216, 66.771387, 78.668054, 75.265018, 72.642968, 74.587372, 79.630978, 75.32303, 67.840694, 69.660334, 72.453879, 73.210832, 75.080906, 68.991805, 69.760039, 68.655485, 67.161804, 68.383478, 63.476653, 61.604585, 63.700181, 64.875939, 66.425011, 62.438905, 63.07888, 64.975192, 58.532068, 63.316845, 61.7866, 63.786719, 62.133676, 67.136965, 68.206039, 62.728082, 69.430766, 64.871745, 65.027685, 63.594558, 62.884859, 67.820215, 70.833333, 59.972678, 65.905744, 63.914511, 64.475816, 64.830082, 68.549618, 63.06338, 63.446864, 66.015068, 62.593516, 61.937452, 68.018111, 66.901529, 63.259047, 64.917296, 65.8, 56.432804, 59.081633, 66.787117, 67.962286, 66.382979, 59.525439, 59.508118, 55.191445, 61.288556, 59.924902, 59.756584, 60.053466, 59.630435, 59.805571, 61.106984, 58.592751, 60.025978, 62.637363, 57.530944, 55.424572, 59.731069, 59.781048, 58.26634, 62.975842, 59.657103, 56.356702, 57.070156, 61.296767, 60.531479, 61.637931, 59.933592, 66.049481, 57.33538, 60.679704, 63.84527, 61.19897, 58.17757, 57.954892, 65.969404, 63.575738, 60.084718, 61.830186, 59.884609, 63.02521, 62.661895, 64.186414, 66.176471, 65.467366, 62.57835, 64.13872, 58.596373, 61.955017, 65.909885, 57.179487, 59.240459, 61.926842, 56.199533, 56.576047, 56.229975, 60.172861, 59.976932, 61.366085, 61.573319, 59.117481, 55.612789, 61.852811, 60.126162, 64.80079, 59.733037, 62.022117, 63.141178, 57.433712, 59.015852, 59.087927, 56.62768, 56.607495, 56.673145, 57.046332, 60.870231, 54.893679, 52.784692, 57.847932, 53.612455, 53.62252, 56.524275, 56.870401, 58.952366, 60.446686, 61.205882, 60.060976, 62.859079, 64.484605, 61.297798, 59.865913, 59.027205, 62.253845, 61.62615, 63.973064, 63.595228, 62.886973, 62.709142, 60.047746, 65.832802, 62.810811, 64.254272, 59.53668, 62.268969, 59.906068, 60.251147, 61.683402, 60.289368, 63.538399, 61.743656, 62.784905, 60.640427, 61.488847, 58.871071, 61.801321, 62.398723, 63.319791, 59.914478, 57.956372, 57.185118, 58.423072, 58.337525, 58.245614, 59.462776, 60.582549, 60.936348, 60.166766, 62.914148, 59.239704, 60.565973, 60.797302, 57.280525, 59.540613, 58.263898, 62.47191, 59.500063, 59.527982, 58.2846, 60.068826, 62.521589, 60.153864, 62.441104, 60.862108, 60.24726, 60.945218, 60.494544, 64.633867, 66.318259, 66.526565, 64.157466, 65.505457, 60.843373, 61.932055, 60.62472, 62.805007, 63.479532, 62.675416, 64.805447, 59.5559, 59.593194, 58.460657, 62.374134, 59.975694, 56.451438, 61.04758, 63.328453, 62.649626, 60.146413, 62.247413, 64.187101, 60.8942, 59.601931, 60.272463, 60.978823, 55.8778, 54.065911, 56.309441, 59.258101, 58.145725, 60.478143, 60.385972, 58.957621, 60.895771, 61.816374, 59.441726, 59.004168, 62.967498, 60.169584, 61.497453, 61.020521, 59.010281, 60.493402, 63.53697, 62.444147, 64.712086, 64.647903, 62.146459, 61.680432, 63.246944, 61.926283, 59.800372, 61.813916, 63.40069, 61.318917, 64.367479, 62.318975, 61.956522, 61.785581, 60.965555, 60.068123, 57.129446, 58.692235, 56.08202, 58.459756, 60.538453, 60.340261, 58.979402, 59.624413, 57.262016, 58.002707, 58.281315, 63.227595, 61.581747, 60.368613, 62.837569, 60.891337, 63.320119, 60.461391, 61.404446, 63.389405, 62.360894, 62.398807, 57.015639, 57.388919, 61.009951, 60.018233, 60.164916, 58.988002, 63.117986, 57.624712]}
posts_by_day_df = pd.DataFrame(posts_by_day_data)

# Posts by hour data
posts_by_hour_data = {
    "Hour": list(range(24)),
    "Post Count": [120500,121644,116328,111173,108427,102887,99499,94427,91877,85050,88392,92632,94797,101734,110502,114670,117059,114666,113476,115241,111101,108530,104316,101279]
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
    st.write(f"Average Likes per Post: {avg_likes_per_post}")
    st.write(f"Average Likes per SFW Post: {avg_sfw_likes_per_post}")
    st.write(f"Average Likes per NSFW Post: {avg_nsfw_likes_per_post}")
    st.write(f"Date with Most Posts: {date_most_posts}, (11111)")
    st.write(f"Average Posts per Day: {avg_posts_per_day}")
    st.write(f"Bottom 25%/Median/Top-25% likes/post: {likes_percentile}")

elif selected_page == "Top Users":
    st.subheader("%", help = "These are two different sets")
    st.write("Top 100 users contributed 492475 posts (19.39%) and 10513319 likes (34.36%)")
    st.write("Top 200 users contributed 691986 posts (27.24%) and 14137932 likes (46.21%)")
    st.write("Top 500 users contributed 1046820 posts (41.21%) and 19175784 likes (62.67%)")
    st.subheader("Top 100 Users by Number of Posts")
    st.dataframe(top_users_df, hide_index = True)
    st.subheader("Top 100 Users by Number of Likes")
    st.dataframe(top_users_likes_df, hide_index = True)

elif selected_page == "Posts by Day":
    st.subheader("Posts by Day")
    st.line_chart(posts_by_day_df.set_index("date")[["total_posts", "nsfw_posts"]])

elif selected_page == "Posts by Hour":
    st.subheader("Posts by Hour")
    st.bar_chart(posts_by_hour_df.set_index("Hour"))
